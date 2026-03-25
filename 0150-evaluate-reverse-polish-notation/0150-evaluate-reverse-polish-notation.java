class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int n=tokens.length;
        for(String t: tokens){
            if(t.equals("+") || t.equals("-") || t.equals("/") || t.equals("*")){
                int a=stack.pop();
                int b=stack.pop();
                switch(t){
                    case "+": stack.push(a+b); break;
                    case "-": stack.push(b-a); break;
                    case "/": stack.push(b/a); break;
                    case "*": stack.push(a*b); break;
                    default:break;
                }
                System.out.println(stack.peek());
            
            }
            else{
                
                stack.push(Integer.parseInt(t));
                System.out.println(stack.peek());
            }

        }
        return stack.pop();
    
    }
}