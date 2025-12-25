def find_duplicate(nums):
	"""Return the first duplicate number found in list `nums`, or None if no duplicate."""
	seen = set()
	for n in nums:
		if n in seen:
			return n
		seen.add(n)
	return None


if __name__ == "__main__":
	# Example usage — replace `sample` with any list of ints to test
	sample = [1, 3, 4, 2, 5, 3]
	print("List:", sample)
	dup = find_duplicate(sample)
	if dup is None:
		print("No duplicate found")
	else:
		print("Duplicate:", dup)