//

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response should be an array", function () {
    pm.expect(pm.response.json()).to.be.an('array');
});

pm.test("First user should have an ID", function () {
    pm.expect(pm.response.json()[0]).to.have.property("id");
});
