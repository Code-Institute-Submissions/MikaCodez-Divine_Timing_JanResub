# Testing for Divine Timing Ecommerce Store


## Validator Testing

### LightHouse

Testing was achieved through Google Chrome Lighthouse. Initially had to make sure that testing was done in Incognito browser as
my extensions were interfering with the testing giving the site low scoring.

•Website works on browsers such as Edge, Firefox, Safari and Google Chrome.

•Website content is easy to read and follow.

•Links between pages work harmoniously.

![lighthouse 1](https://user-images.githubusercontent.com/65243328/185663989-def71dd2-2cca-4a02-9a39-081d852d4f14.JPG)


### W3C MARKUP TOOLS

No major visible Errors where shown for Nu HTML validator, mainly just some warnings for javascript tag uses.
Home page:
![nuhtmlvalidator 1](https://user-images.githubusercontent.com/65243328/190242666-5ef79993-2875-4229-9f32-a94fce49bba3.JPG)

Products:

![nuhtmlvalidator 2](https://user-images.githubusercontent.com/65243328/190242672-9bbc523e-68cc-4830-9adb-667567f7ee97.JPG)

Profile:

![nuhtmlvalidator 3](https://user-images.githubusercontent.com/65243328/190242673-01e06ae9-17f6-4fcd-a3dd-7d0f0ec67cc1.JPG)

Bag:
![nuhtmlvalidator 4](https://user-images.githubusercontent.com/65243328/190242679-a73d75bd-b0bc-4f29-8d68-08a9e5513665.JPG)



## Python Validator PEP8
  
  Hardly any errors discovered for Python testing but pretty much the same as W3C Validator, mainly blank line space errors and line too long errors
  however that could not be helped due to the code/ imports executed in order to make code work. Other than that everything came back clean.
  
  Admin.py:
![adminpytest](https://user-images.githubusercontent.com/65243328/185669163-ebddeb82-a67c-4a70-ba0f-6e099fc9dbab.JPG)

  
  Apps.py:
![apppytest](https://user-images.githubusercontent.com/65243328/185669184-d71c19d0-436b-46cb-ac86-b5392d13fcc3.JPG)

  
  
  models.py:
There was one line error regarding the Line being too long however this couldn't be helped due to the Models code.
  I tried putting it through pyformatter however it was displaying an error in regards to this.
  
  ![modelspytest](https://user-images.githubusercontent.com/65243328/185669199-cc02794a-05d7-49fa-919e-3541991584cb.JPG)

  
  Urls.py:
![urlspytest](https://user-images.githubusercontent.com/65243328/185669220-96840b3a-64ff-45db-9dfe-00f3712e87e4.JPG)

  
  wsgi.py:

![wsgipytest](https://user-images.githubusercontent.com/65243328/185669233-77dbdc55-4cc7-41ad-919c-1558022d9005.JPG)


## JavaScript Validation
I have carried out JavaScript validation on all JavaScript files and JavaScript code within HTML files using JSHint. No errors came back, just a warning.

![jstest](https://user-images.githubusercontent.com/65243328/185670892-4b8f3abc-3f20-4c9a-84b6-d1e17f5b2859.JPG)

  
## User Story testing
  
  ### Admin
As a Site Admin I can approve or disapprove users of signing up to the website and creating their own profile.

As a Site Admin I can create, read, update and delete Products via the Product management page and the admin page, in order to add new products to the store.
![prodmanage1](https://user-images.githubusercontent.com/65243328/185662439-d6ca84f5-3eb9-4ec8-8f5a-be100809bc5d.JPG)
![prodmanage2](https://user-images.githubusercontent.com/65243328/185662457-55e05015-5af3-42a3-a9a6-02f5bc55a8cd.JPG)


![adminpage](https://user-images.githubusercontent.com/65243328/185662343-d6b8b5da-56a3-44e0-9370-74b10f41c211.JPG)


   ### User
  As a Member User I can register an account so that I can view my previous order history, make new purchases and also update my profile and delivery details.
  I am also required as a member user to sign up in order to purchase products otherwise I will be prompted to register an account.
  ![prof1](https://user-images.githubusercontent.com/65243328/185662862-bcf95c2c-b560-440b-8ba4-e240912f71fb.JPG)

  ![profile order history](https://user-images.githubusercontent.com/65243328/185662997-8d9698b1-bb47-4eda-acc3-11d4792de785.JPG)

  
  
 ### General Browser User
  As a General user I can browse the site, view the page and browse products that I would like to purchase in the future.
  However in order to make a purchase I will be prompted to register an account.
 
  ![signup2](https://user-images.githubusercontent.com/65243328/185671810-2b4a7e1d-f257-4092-b4c5-35ef1381c358.JPG)


## Responsiveness
  
 Site performs well across all different platforms.
  
  Mobile:
![mobile](https://user-images.githubusercontent.com/65243328/185660279-c5ef10a6-a91c-421d-85ba-19428d7acf03.JPG)

  
  Tablet:
![tablet](https://user-images.githubusercontent.com/65243328/185660287-9a3f124d-3c96-4b05-bd2e-27c4954dd5ef.JPG)

  
  Desktop:

![divin3](https://user-images.githubusercontent.com/65243328/185660336-50329ece-c848-424b-82a3-1ac26c363dc7.JPG)



## Current Bugs and Issues
Only issues seem to be facing at the moment is the rendering of comments on individual product pages.
Hopefully will have this operating normally when 2nd edition of site is launched.

  ![addcomment 2](https://user-images.githubusercontent.com/65243328/190250225-65c27c17-763d-4346-bffe-159e3118fa09.JPG)
  

## Update ##
Issue with comments section has now been fixed and comments are now operating as normal on the frontend side and on the backend side.

![image](https://user-images.githubusercontent.com/65243328/204845881-0260d175-eb13-4224-b271-476318f64324.png)

Newsletter Pop-Up Form now working, as implemented from the code of Mailchimp.

![image](https://user-images.githubusercontent.com/65243328/204848189-b2c99d5a-dd4c-42d4-a4a2-90050b45333d.png)

WishList template now in place with option to allow users to Add to wishlist

![wishlist test](https://user-images.githubusercontent.com/65243328/206454634-8e2926c0-2096-4463-abb5-dd52bf2715f7.JPG)

Purchase Functionality also working fine.
![purchase new test](https://user-images.githubusercontent.com/65243328/206454788-68bbce2d-7940-4e88-9103-31bccba5ff93.JPG)





[Back to Readme](https://github.com/MikaCodez/Divine_Timing/blob/main/README.md)
