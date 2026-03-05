class Solution {
  public boolean isNumber(String s) {
    s = s.trim();
    if (s.length() == 0) return false;
    boolean Num = false;
    boolean Dot = false;
    boolean E = false;
    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      switch (c) {
      case '.':
          if (Dot || E)
            return false;
          Dot = true;
          break;
        case 'e':
        case 'E':
          if (E || !Num)
            return false;
          E = true;
          Num = false;
          break;
        case '+':
        case '-':
          if (i > 0 && s.charAt(i-1) != 'e' && s.charAt(i-1) != 'E')
            return false;
          break;

        default:
          if (!Character.isDigit(c))
            return false;
          Num = true;
      }
    }

    return Num;
  }
}