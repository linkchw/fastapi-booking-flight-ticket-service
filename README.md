## Create a User
```json
{
  "username": "alireza.d",
  "email": "alireza@gmail.com",
  "name": "Alireza",
  "phone_number": "0091233123",
  "password": "randowm@dkjfa123"
}
```

## Submit an Order
```json
{
  "code": "ORD123",
  "price": 200.75,
  "user_id": 1,
  "tickets": [
    {
      "ticket_number": "TICKET123",
      "passenger": {
        "name": "John Doe",
        "national_id": "123456789",
        "age": 30,
        "gender": "Male"
      }
    },
    {
      "ticket_number": "TICKET124",
      "passenger": {
        "name": "Jane Smith",
        "national_id": "987654321",
        "age": 28,
        "gender": "Female"
      }
    }
  ]
}
```
