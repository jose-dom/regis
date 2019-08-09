from django.db import models
from django.core import validators
from django import forms
from multiselectfield import MultiSelectField


##Models
class Visitor(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)

    options1 = (
        ("Job Placement Assistance", 'Job Placement Assistance'),
        ("Resume Preparation", 'Resume Preparation'),
        ("Mock Interviewing", 'Mock Interviewing'),
    )
    options2 = (
        ("Construction", 'Construction'),
        ("Pre-Apprenticeship", 'Pre-Apprenticeship'),
        ("Microsoft Office Certification", 'Microsoft Office Certification'),
    )
    options3 = (
        ("Public Income Benefits Screening",'Public Income Benefits Screening'),
        ("Employment Services and Career Improvement",'Employment Services and Career Improvement'),
        ("Financial Workshop",'Financial Workshop'),
        ("Financial Coaching",'Financial Coaching '),
    )
    options4 = (
        ("Start Saving on a Shoestring",'Start Saving on a Shoestring'),
        ("Your Choices and Your Cha-CHING!!",'Your Choices and Your Cha-CHING!!'),
        ("Early Career Guide to Becoming Financially Fit",'Early Career Guide to Becoming Financially Fit'),
        ("MoneyWISE is a Family Affair)",'MoneyWISE is a Family Affair'),
        ("Be a Budget BOSS",'Be a Budget BOSS'),
        ("Managing Credit and Debt - The RIGHT Way",'Managing Credit and Debt - The RIGHT Way'),
        ("What's in YOUR B.A.G.?  Planning, Saving and Getting Resources for Your  Big, Audacious Goals",'Whats in YOUR B.A.G.?  Planning, Saving and Getting Resources for Your  Big, Audacious Goals'),
        ("Miss Independent:  A Womans Guide to Saving and Investing",'Miss Independent:  A Womans Guide to Saving and Investing'),
        ("Protecting Your Assets; Protecting Your Family",'Protecting Your Assets; Protecting Your Family'),
        ("Your Financially Ever After ",'Your Financially Ever After'),
    )
    options5 = (
        ("Rental Counseling",'Rental Counseling'),
        ("Homebuyer Counseling",'Homebuyer Counseling'),
        ("Foreclosure Counseling",'Foreclosure Counseling'),
    )
    options6 = (
        ("High School Equivalency Program",'High School Equivalency Program'),
        ("Job Readiness for Teens)",'Job Readiness for Teens'),
    )
    options7= (
        ("Early Childhood Center",'Early Childhood Center'),
        ("Newark Kids Code",'Newark Kids Code'),
    )
    options8 = (
        ("Youth Programs",'Youth Programs'),
        ("Adult Programs",'Adult Programs'),
        ("Early Head Start",'Early Head Start'),
    )
    purpose1 = MultiSelectField(choices=options1, default="None", verbose_name="Employment Programs", blank=True)
    purpose2 = MultiSelectField(choices=options2, default="None", verbose_name="Workforce Training Programs", blank=True)
    purpose3 = MultiSelectField(choices=options3, default="None", verbose_name="Financial Opportunity Center", blank=True)
    purpose4 = MultiSelectField(choices=options4, default="None", verbose_name="Workshops", blank=True)
    purpose5 = MultiSelectField(choices=options5, default="None", verbose_name="Housing", blank=True)
    purpose6 = MultiSelectField(choices=options6, default="None", verbose_name="Young Adults Program", blank=True)
    purpose7 = MultiSelectField(choices=options7, default="None", verbose_name="Youth Education", blank=True)
    purpose8 = MultiSelectField(choices=options8, default="None", verbose_name="Volunteering", blank=True)
    choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    gender = models.CharField(max_length=100, choices=choices, default="Other")
    address = models.CharField(max_length=100, default="")
    referral = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.email