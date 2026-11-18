class Solution {
    public List<String> partitionString(String s) {
        StringBuilder sb=new StringBuilder();
        Trie trie=new Trie();
        List<String> result=new ArrayList<>();
        for(char c:s.toCharArray()){
            sb.append(c);
            if(!trie.search(sb.toString())){
                trie.insert(sb.toString());
                result.add(sb.toString());
                sb=new StringBuilder();
            }
        }
        return result;
    }
}


class Trie{
    Node root;

    Trie(){
        this.root=new Node();
    }


    void insert(String word){
        int n=word.length();
        Node crawl=this.root;
        for(char c:word.toCharArray()){
            int idx=c-'a';
            if(crawl.children[idx]==null){
                crawl.children[idx]=new Node();
            }
            crawl=crawl.children[idx];
        }
        crawl.isWord=true;
    }


    boolean search(String word){
        Node crawl=this.root;
        for(char c:word.toCharArray()){
            int idx=c-'a';
            if(crawl.children[idx]==null){
                return false;
            }
            crawl=crawl.children[idx];
        }
        return crawl.isWord;
        
    }
}

class Node{
    boolean isWord;
    Node [] children;

    Node(){
        this.isWord=false;
        this.children=new Node[26];
    }
}