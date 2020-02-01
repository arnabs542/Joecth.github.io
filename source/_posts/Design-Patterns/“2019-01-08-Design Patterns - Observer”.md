---
layout: post
categories: DesignPattern
ag: []
date: 2020-01-08
---



### Observer Pattern

Still for OCP -- Open Close Principle, which means, open for extension, close for modification.

Define 1vsMany, such that all observers receives notification when the observable getting update.



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200116114053868.png" alt="image-20200116114053868" style="zoom:67%;" />





```java
    abstract class Subject {
        private Vector obs = new Vector();

        public void addObserver(Observer obs){
            this.obs.add(obs);
        }
        public void delObserver(Observer obs){
            this.obs.remove(obs);
        }
        protected void notifyObserver(){
            for(Observer o: obs){
                o.update();
            }
        }
        public abstract void doSomething();
    }

    class ConcreteSubject extends Subject {
        public void doSomething(){
            System.out.println("被观察者事件反生");
            this.notifyObserver();
        }
    }
    interface Observer {
        public void update();
    }
    class ConcreteObserver1 implements Observer {
        public void update() {
            System.out.println("观察者1收到信息，并进行处理。");
        }
    }
    class ConcreteObserver2 implements Observer {
        public void update() {
            System.out.println("观察者2收到信息，并进行处理。");
        }
    }

    public class Client {
        public static void main(String[] args){
            Subject sub = new ConcreteSubject();
            sub.addObserver(new ConcreteObserver1()); //添加观察者1
            sub.addObserver(new ConcreteObserver2()); //添加观察者2
            sub.doSomething();
        }
    }
```

ref from: https://wiki.jikexueyuan.com/project/java-design-pattern/observer-pattern.html





