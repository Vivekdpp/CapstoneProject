# CapstoneProject

API Endpoints:

(1) restaurant/menu/   
(2) restaurant/menu/1 [for Single-menu-item]
(3) restaurant/booking/tables/

--> If you want to add new item with specific ID: you can do this by this link in Insomnia: restaurant/menu/ and pass the JSON Body: 
                                                                                                                        {
                                                                                                                        	"ID": "5",
                                                                                                                        	"title": "ItalianPasta",
                                                                                                                        	"price": "11.99",
                                                                                                                        	"inventory": 20
                                                                                                                        }
                                                                                                                        
                                                                                                                        Then Press POST. 
                                                                                                                        
--> If you want to generate a token, you can do like this in Insomnia: 
JSON Body: 
{
		"username" : "your_username",
	  "password": "your_password"
	
}

Select POST from DropDown: http://127.0.0.1:8000/restaurant/api-token-auth/    and then Hit the send button. You will get the token for that user. 
