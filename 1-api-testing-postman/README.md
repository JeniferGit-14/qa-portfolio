# 📡 API Testing with Postman

## ✅ Objective
To test a sample API using Postman, validate status codes, and write basic test scripts.

## 🛠️ Tools Used
- Postman
- JavaScript (for test scripts)

## 📋 What I Did
- Sent a GET request to the User List API: `https://reqres.in/api/users?page=2`
- Validated the response status (200 OK)
- Verified JSON response properties (page, per_page, and user data)

## 🧪 Sample Test Script
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response contains 'page'", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("page");
});
