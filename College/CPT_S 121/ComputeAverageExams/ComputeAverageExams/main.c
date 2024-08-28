/*
	Author: Logan Meyers
	Date: 08/26/2024

	Description: This program prompts the user for 3 exam scores, computes the average of the 3 exam scores,
	             and displays the average to the screen
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>  // printf(), scanf()

int main() {
	// decalare variables
	int score1 = 0, score2 = 0, score3 = 0;

	// 1. prompt the suer for exam score 1
	printf("Please enter exam score 1: ");

	// 2. get the score for exam 1 from the user
	scanf("%d", &score1);

	// 3. prompt the user for exam score 2
	printf("Please enter exam score 2: ");

	// 4. get the score for exam 2 from the user
	scanf("%d", &score2);

	// 5. prompt the user for exam score 3
	printf("Please enter exam score 3: ");

	// 6. get the score for exam 3 from the user
	scanf("%d", &score3);

	// 7. sum up the scores
	int total = score1 + score2 + score3;

	// 8. average the scores
	int average = total / 3;

	// 9. output average
	printf("Here is your average: %d", average);
	
	return 0;
}
