func getSum(a, b int) int {
	carry = 0
	while (a != 0) {
		carry = a & b
		b = a ^ b
		a = carry << 1
	}
	return b
}
