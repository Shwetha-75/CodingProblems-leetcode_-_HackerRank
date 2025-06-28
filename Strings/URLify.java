class URLify{
   ''

    public String urlifyActivity(String input,int n){

          StringBuilder string=new StringBuilder();
          int index=0;
          while(index<n){
               if(input.charAt(index)==' '){
                    string.append("%20");

               }
               else{
                string.append(input.charAt(index)+"");

               }

               index++;
          }
          return string.toString();
    }
}