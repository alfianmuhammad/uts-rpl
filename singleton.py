package main

import (
	"fmt"
	"sync"
	"time"
)

var lock = &sync.Mutex{}

type Single struct {
	Conn string
}

var singleInstance *Single

func getInstance() *Single {
	// inisialisasi lock untuk mengatasi thread safe
	lock.Lock()
	// melepaskan kunci setelah inisialiasi
	defer lock.Unlock()

	if singleInstance == nil {
		singleInstance = &Single{"Koneksi Database"}
		fmt.Println("Instansiasi sudah terbuat sekarang")
	}

	return singleInstance
}

func main() {
	go func() {
		for i := 0; i < 100; i++ {
			time.Sleep(time.Millisecond * 600)
			fmt.Println(*getInstance(), " - ", i)
		}
	}()

	go func() {
		fmt.Println(*getInstance())
	}()

	fmt.Scanln()
}