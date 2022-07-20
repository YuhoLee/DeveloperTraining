package com.ssafy.ws05.step3;

public class ISBNNotFoundException extends Exception{
    private static final long serialVersionUID = 1L;
    
    public ISBNNotFoundException() {
        super("해당 도서가 존재하지 않습니다.");
    }
}
