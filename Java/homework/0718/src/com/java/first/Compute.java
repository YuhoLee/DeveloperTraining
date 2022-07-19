package com.java.first;
import java.util.Scanner;

public class Compute {
	private int n1;
	private int n2;
	private Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		Compute c = new Compute();
		c.calc();
	}
	
	private void calc() {
		String[] str = sc.nextLine().split(" ");
		this.n1 = Integer.parseInt(str[0]);
		this.n2 = Integer.parseInt(str[1]);
		this.mult();
		this.share();
	}
	
	private void mult() {
		System.out.println("곱="+this.n1*this.n2);
	}
	private void share() {
		int res;
		
//		if(this.n1 > this.n2) { res = this.n1 / this.n2; }
//		else { res = this.n2 / this.n1; }

		res = this.n1 / this.n2;
		System.out.println("몫="+res);
	}

}
