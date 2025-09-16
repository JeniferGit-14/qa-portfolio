### Defect Report 1

**Title:** Bill not updated after payment

**Steps to Reproduce:**
1. Submit payment via POST /payment
2. Check GET /billing/{id}

**Expected:** Status = Paid
**Actual:** Status remains Unpaid

**Severity:** High
