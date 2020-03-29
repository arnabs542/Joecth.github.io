---
layout: post
categories: Microservice
tag: []
date: 2016-03-10

---



MSA

> Building microservices in Python. Inthis video we're going to be focusing onthe microservices approach, we're goingto be investigating what is a microservice, and explain the advantages anddisadvantages of using microservices. Now themicroservice architecture can be shortened toMSA, it is a variant of the serviceorient architecture, or SOA. Its purposeis to decouple and MA July's systemservices and it follows the UNIXphilosophy. Some of the advantages of using microservices is that itseparates the system concerns. Alsomicroservices our language and design agnostic, so you can have multiplemicroservices that are designed in differentlanguages. We isolate and decouple our deployments because each microserviceis separate. Smaller services can besimpler to understand. Basically you're moving away from the monolithicarchitecture, and you're simplifying yourapplication in a single concern. Itallows for continuous delivery because a microservice can be available whenother microservices are not. It alsoallows for horizontal scalability, so youcan scale your microservices to suit the needs and demands of your system.Let's focus on some of these in a littlebit more detail. So splitting a system into mini Services separates andisolates the system responsibilities, meaning that each responsibility of asystem now has its own little place tolive. Services do not have to conform tothe same technologies that other services require, you could have amicroservice written in one programming language, you could have another onewritten in another programming language,they all use perhaps a common API kindof communication structure, but the actual technologies that these microservices use can be completely different, which means that you can actuallyyour microservices to best suit theneeds for your system. Services can bedeployed independently and continuously,which means that a service doesn't haveto rely on another service to be active.You can continuously update your code inone service without having huge impactto other services in your system. Smaller services are easier to understand asthey are disconnected from a monolithic application, which means that you canactually microscopically understand parts of the application, you don't haveto understand the whole application, just the services that you are working with,which means that it's perfect for teamsof multiple developers. And services canbe scaled independently. If, for instance,you have a lot of registration going on, then you would scale your registrationservice. If, for instance, you had a lot of demand on a particular other service,then you could scale that too, but you're not affecting the other services byscaling singular services at once. So now let's go and focus on some of thedisadvantages of using microservices.For one there is more overhead, and alsoit can be very difficult to test microservices together. There are more security points to consider and this canlead to complicated and duplicated dependencies across your microservices.By splitting an application into microservices you're increasing the amount ofcommunication between those services in the background, and this can often leadto more load time. Testing Serviceintegration can also be a challenge, themore services you have the bigger theattack surface. More services means moretechnical debt, when I said in the advantages that you can have multipleprogramming languages across your microservices, you are then also creatingoverhead on the maintenance of thoseservices. And lastly you will probably face duplication of code dependenciesacross services, which means that you might have codethat is the same in different services because they are a dependent that isrequired for that microservice to run. In the next video we're going to be





![image-20200311122557154](https://tva1.sinaimg.cn/large/00831rSTgy1gcpvihqcmej31660mojx5.jpg)

> In this video, we're going to be discussing how microservices arestructured. We're going to be exploringthe typical structure of a microservice,explain each of the layers within amicroservice, and talk about thecommunication between microservices. Asan oversimplification, a microservicehas three layers. The first is a communication layer, then we have aprocessing layer, and then we have astorage layer. In a over simplistic casewe could have a set up like so, where youhave a front-end website, and perhaps twoor three microservices, each service hasan API that is the communication. We havea process layer which is typically acontrol layer, and then we have a DB, which is the database. Now not allservices require a storage layer, theinvoice service for example just needs an API, and a way of processing thoseinvoices. The communication layer istypically a RESTful API, and it shouldfollow the HTTP response and requestprotocols. They can also make internalservice calls as well, so for instance you could have a microservice talkingto another microservice within yourapplication. They may allow access to andfrom external sources, and they should bewell documented. And of course each APIthat you have should be consistent throughout your application. Theprocessing layer processes are therequests given by the API. It alsogenerates the responses that APIendpoint has, and it also may use othersystems such as queues and libraries tohandle the data that it is given. Thestorage layer is optional, your microservice may not need to persist data.Each service should however have its owndatabase if it is required. You shouldn'thave a microservice using anotherdatabase within another microservice.Of course it could also be file storageas well. If you think of the entry pointsinto your application typically you mayhave a front-end website, you might alsohave a back-end website, and of courseyou could have a mobile app. In order tohandle the requests from these entrypoints, you typically have a gateway. Nowthis gateway will then send thoserequests to the relevant microservices.
>
> ![image-20200311122743720](https://tva1.sinaimg.cn/large/00831rSTgy1gcpvkkczpij31800msagu.jpg)
>
> The API gateway can ensure securityamongst these API requests, and also itcan be used to map the relevant requeststo the relevant microservice API.Notice that this setup has communicationbetween the user service, the orderservice, and the invoice service. By usinga gateway we no longer have to haveinter service communication. What we cando is use the gateway in order to trackand transfer communication between theseservices. So the API gateway is an entrypoint for API endpoints, it orchestratesthe API requests, and it can alsooptimize the request by collapsing knownrequests, we no longer have to makesingle requests quite often, what we can do is collapse them down into a singlerequest if we wanted to. It also abstracts the implementationfrom the interface. Other things that wecan use our API gateway for include loadbalancing and traffic control, we canalso handle authentication, and we canalso start logging our API requests. Whatdo I mean by orchestrating API requests? Wellthe API gateway could be used to sendportions of traffic to differentservices. Let's say for example you have this user service, and you want toupgrade its features. You want to try all those features out, and so what you coulddo with the mobile app is send 90% oftraffic to the old user server, and you could be sending 10% of trafficto the new user service, and then youcould be monitoring those API requests,and monitoring how the users interactwith your new features. And what do Imean by collapsing API requests? Well inthis case we have a user service, we havean order service, and an invoice service, each of these are going to return theirown API responses. So we have a userobject a invoice object in an orderobject all coming back as a JSON. By having an API gateway what we could dois collapse those API responses into asingle response, which means that there is a single API request to get thosethings, because the communication between the services is handled with the Gateway,which means that we have a single response here an invoice in order and auser. Of course we can also add someclever caching at this level as well. Inthe next video we're going to be looking at what tools are used to build Hide transcript In this video, we will take a look at how microservices are structured. Explore the typical structure of a microservice Get explanation to each layer in a microservice Discuss communication between microservices



## What Tools Are Used to Build Microservices in Python?

- Flask, Swagger, JSON, SQL and Docker



## Designing the Order Management Microservices

Play Mute Remaining Time -5:15 Playback Rate1.25x CaptionsFullscreen Designing the order management microservices, the order managementsystem. In this video, we're going to be taking a look at the requirements thatmake up the system specification for theorder management microservices. We're going to be looking at the overalldesign of each of the microservices, and at the end we're going to have ademonstration of how this system couldbe used. The basic requirements of this order management system is that it ismade up of three services. Each serviceshould have its own business domain, andeach service should not be tightly coupled to another service. A serviceshould be able to run independently fromthe other services. So we've got threeservices here, a user service, a productservice, and an order service. These services will make up our ordermanagement system. The overall requirements for the system is that auser can log in, a user can register, anda user can log out, a user can browse theproducts, and a user can add a product to an order, a user can also remove aproduct from an order, and a user can adjust the quantity of an order item, andfinally a user can place an order. Basedon the fact that these services are going to be independently housed andcreated we can start having some rulesthat define how these services shouldbehave. 

**So **

**if the product service goes down a user must still be able toregister. **

**If the order service fails thenall the products must still be shown, and **

**users should be able to login even if the order or product services are down.**

Let's take a look at the design of thesemicroservices. Firstly each service should be self-contained.A service should not depend on anotherservice to function, and services shouldbe lightweight in terms of code. Here we can see the three services each having adatabase and their own processes, we canalso see the API endpoints that connectto the front-end website, and we can see that each of these things aredecoupled from one another. The front end should be shown regardless of servicestate and the service data should be held within the service, the processeswithin the service should only be performed within the service, weshouldn't have other services that we use just to get a service to work. Inbetween the front end website and theservices we can have an API gateway, moreon this later on in the course. This isthe application running in its entirety,all of the microservices are currently built and running, and I'll talk abouthow to deploy microservices later on in the course.For now though, let me just give a walkthrough of what the application cando. So we have the home page here this is listing out the products from theproduct service. I can click view moreand then I can add that to my own cart.Obviously I need to be logged in, so Ineed to have a user record in the userservice. So we click on register, I'm justgoing to create myself a temporary user,with the user name of temp 20, the firstname of Peter, and the last name ofFisher, I'm just going to have a verytemporary email address so test at temp20 com, and then the password, I'm just going tohave as test, we hit register that'sgoing to submit the page, that's going tosave a record in the user service. Sothat's firing the API request to theuser service from this front-end website.We can now login using the username thatwe've supplied, so temp 20 and thepassword of test. If I hit login that should now log us into the system, sowelcome back temp 20, and we can now addthings to our cart. So let's add the bananas, let's add that to the cart, wecan add another one to the cart if we wished, we click back on the homepage,let's add some coffee, and then finallywhat I can do is I can click checkout,and this will set the order to becreated and published. So let's hit checkout this will then process the order andgive us this thank you message. If I haven't got anything in the cart myclick checkout it'll say no order found,so there is logic to handle those usecases. Also what we can do is log out from the system, by clicking on loginI can then log back in to that user account and I can create another order.The order that has been previouslycreated has been published and processed, which means that a new order that getscreated is completely different from anorder that already exists. In the next few videos we're going to be drillingdown even further into each one of these services to see what their features are.



## The User Registration Service

In this video, we're going to be taking a look at the featureset that makes up the user service. We're going to be looking at the **design of the user service** as well, and after that we're going to be discussing and exploring future improvements that wecan have on this user service. 

Let's take a look at the features that this user service has to offer. First of all, we canregister a user and that user can then login to the system. The user can alsolog out and we can retrieve informationabout that logged in user. The userregistration requires a database to holdthe user information, it also requires aunique identifier to identify the user,so this could be an email address or auser name. It also requires a HTML formin the front-end, this must handle a postrequest and a get request. The user loginfeature also requires a database to holdthe security information of that user, so here I'm talking about passwords, I'mtalking about usernames, and I'm talking about access tokens. We must send backauthentication data if the login wassuccessful, and upon successful login auser session must be instantiated on thefront-end. It also requires the front-endto have a HTML login form that can alsohandle both post and get requests. The user logout is slightly simpler, allwe're doing here is we're stopping the front-end session which means that theuser can no longer access secure areas of the website, and when we're retrievinguser data we must only return the dataof the logged in user. So they are the features, let's take a look at the APIendpoints. Here we got three post requests and one get requests. The post requests will create a user that's going to be used in the user registration, wealso have user logout and login. The get request however is going to retrieveuser information, so that is API slashuser. The user registration API endpointwill be processed similar to this. So in the front endthe user submits a form, if the form is valid then it goes on to check if theform is unique. So here we're checking the unique identifiers of the user. Ifany of those are incorrect then wedisplay an error back to the front end,if they are correct however we go andsave the user to the database. Once the user has registered into the system theuser can now login to the system. So here the user submits the login form andagain it checks if the form is valid. Ifthe form isn't valid then we display anerror to the front end, however if it is valid then we start the session on thefront end, and we redirect the user to a secure area. The logout process isextremely simple. Here the user clicks a logout button from that point on thesession is stopped and we redirect theuser to the public area, which means that the user can no longer access their ownareas and find their own orders. The onlyget request that this user service has is to retrieve the current locked inuser. Here the user is making a requestwhich has headers. The headers willidentify if the user has beenauthenticated, if not we will display anerror back to the front-end, and if it is then we return the user data. There are anumber of future improvements that we can do to this user service. Some ofwhich include a forgotten password feature, we can also issue passwordresets, and we can allow logins throughsocial accounts. So this is a third-party logins using things like Facebook,Twitter, Linkedin and GitHub. We couldalso have different user roles and one of those roles could be an admin role,that admin role could supply an optionalparameter be it a user name or an ID tothe get request which gets the user information. This means that the adminscan retrieve different user accounts if

![image-20200311201420855](https://tva1.sinaimg.cn/large/00831rSTgy1gcq963wpqej31vs0u0wlh.jpg)



## The Product Service

**The product service only has two features.** 

The firstfeature returns a single product, the second feature will return multiple products. 

When we're returning all of theproducts we do so in a JSON format, hereis a typical response that we get fromthe API call. Here we have an array ofresults. When we return a single productwe only return a single result. Both API endpoints are get requests and the single product API endpoint takes a Product ID, this is used to identify which product will be returned. 

**Future improvements** could include pagination,this could be both paging and limits, this could be added to the multipleproduct API endpoint, we can also addcaching between the database calls, thiswill speed up subsequent database callsthat retrieve the same page, or the same data set. And of course we could addfilters to the API endpoints, this couldsort and filter the returned data. In thenext video we're going to be focusing on



## The Order Service

In this video, we're going to be discussing the feature setof the order service, we're going to be taking a look at how this service isdesigned, and we're going to be exploring future improvements that this orderservice could have. So let's take a look at the features. 

An order can be created, an item can be added to an order, and anorder can be updated. A single order can also be returned. So we have create, add,update and get. 

So we must only allow logged in users to create an order.Orders can be created without orderitems, so this would be an empty order. Anorder will also have a total cost, whichis the sum cost of all the other orderitems. 

Order items can only be added toan order if you are logged in, an order item can also be added to an existing order, and if an order doesn't exist when the order item is being added, then a new order is created. An order item quantityand total cost is required for everyorder item, and the order total is recalculated when a new item is added tothe order. 

We must only allow logged-inusers to update orders. Quantities can beadjusted and order items can be removedfrom the order. The order total must berecalculated when the order is updated.

We must only return the order if theuser is logged in. The total quantity will be used in the front-endas a basket counter, so this will show onthe front-end website how many items arein the users basket. 

The API endpointsfor the order service are both postrequests and get requests. **The add item,update, and order creation API endpoints,they are all post requests, however whenwe are retrieving an order that is a getrequest.**

**Future improvements** for the order service could include merging both theupdate and add item endpoints together,multiple orders could be made and savedin a draft state, and this might requirethe orders to have their own order statuses. In the next video we're goingto be discussing how the order management system in its entirety could



## How the order management service could be improved?

How the order management system could be improved. In this video, we're going to bediscussing some potential issues with this order management system. We're goingto be looking at some future improvements that we could do, and we'realso going to explore some of my recommendations. 

Some of the potential **issues** could be that 

- multiple orderscannot be made at the same time, this order management system requires that a single order is made by a single user at any one point. 

- orders cannot have any statuses, which means that you can't havean order in a pending state or as atdraft state, and 

- a specific user cannot bereturned unless we have the ability todefine roles. Another issue is thissession. 

  Both sessions front-end and APIsessions must be separated, that isn'tvery easy in the current setup. 

Improvements could include 

- adding product stock levels in the product service, 

- we could also add a cachingbetween product database calls, and 

- we could add an API call to fetch previousorders. 

  My recommendations would be toonly use the code in this course for demonstration purposes. Please don't usethis in production, it is not productionready, also ideally what you would haveis separate source control for each ofthese services, and ideally each of theseservices would have its own database. Inthe next set of videos, we're going to be building the order management service,and we're going to be taking a look at the individual microservices, and I'mgoing to be demonstrating the code that Hide transcript In this video, we look at the issues and flaws of the microservices. We explore potential improvements and discuss recommendations. Discuss the potential issues with this setup Look at what improvements could be made Explore recommendations



## Security Monitoring Tools

- zipkin

- raygun

- Elastic search, cabana, log stash, beats

- wireshark

- chaos monkey 

- siege

  ![image-20200312170003754](https://tva1.sinaimg.cn/large/00831rSTgy1gcr9216tyxj314w0l2tah.jpg)

  