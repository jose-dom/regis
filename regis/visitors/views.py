from django.shortcuts import render, redirect
from .forms  import NewUserForm, FirstTimeUserForm
from .models import Visitor
from django.contrib import messages
import datetime

##Connection to AWS
import boto3
import uuid
dynamodb = boto3.resource("dynamodb")
dynamoTable = dynamodb.Table("example")


##Second Form
def index(request):
    form = FirstTimeUserForm()
    first_name, last_name, email, purpose1, purpose2, purpose3, purpose4, purpose5, purpose6, purpose7, purpose8, time = request.session['first_name'], request.session['last_name'], request.session['email'], request.session['purpose1'], request.session['purpose2'], request.session['purpose3'], request.session['purpose4'], request.session['purpose5'], request.session['purpose6'], request.session['purpose7'], request.session['purpose8'], request.session['time']
    if request.method == "POST":
        form = FirstTimeUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            visitor = Visitor.objects.order_by()[len(Visitor.objects.order_by())-1]
            address = visitor.address
            gender = visitor.gender
            referral = visitor.referral
            for a in purpose1:
                dynamoTable.put_item(
                    Item={
                        'id': str(uuid.uuid1()),
                        'firstname': first_name,
                        'lastname': last_name,
                        'email': email,
                        'gender': gender,
                        'address': address,
                        'referral': referral,
                        'timestamp': time,
                        'purpose': str(a),
                    }
                )
            for b in purpose2:
                dynamoTable.put_item(
                    Item={
                        'id': str(uuid.uuid1()),
                        'firstname': first_name,
                        'lastname': last_name,
                        'email': email,
                        'gender': gender,
                        'address': address,
                        'referral': referral,
                        'timestamp': time,
                        'purpose': str(b),
                    }
                )
            for c in purpose3:
                dynamoTable.put_item(
                    Item={
                        'id': str(uuid.uuid1()),
                        'firstname': first_name,
                        'lastname': last_name,
                        'email': email,
                        'gender': gender,
                        'address': address,
                        'referral': referral,
                        'timestamp': time,
                        'purpose': str(c),
                    }
                )
            for d in purpose4:
                dynamoTable.put_item(
                    Item={
                        'id': str(uuid.uuid1()),
                        'firstname': first_name,
                        'lastname': last_name,
                        'email': email,
                        'gender': gender,
                        'address': address,
                        'referral': referral,
                        'timestamp': time,
                        'purpose': str(d),
                    }
                )
            for e in purpose5:
                dynamoTable.put_item(
                    Item={
                        'id': str(uuid.uuid1()),
                        'firstname': first_name,
                        'lastname': last_name,
                        'email': email,
                        'gender': gender,
                        'address': address,
                        'referral': referral,
                        'timestamp': time,
                        'purpose': str(e),
                    }
                )
            for f in purpose6:
                dynamoTable.put_item(
                    Item={
                        'id': str(uuid.uuid1()),
                        'firstname': first_name,
                        'lastname': last_name,
                        'email': email,
                        'gender': gender,
                        'address': address,
                        'referral': referral,
                        'timestamp': time,
                        'purpose': str(f),
                    }
                )
            for g in purpose7:
                dynamoTable.put_item(
                    Item={
                        'id': str(uuid.uuid1()),
                        'firstname': first_name,
                        'lastname': last_name,
                        'email': email,
                        'gender': gender,
                        'address': address,
                        'referral': referral,
                        'timestamp': time,
                        'purpose': str(g),
                    }
                )
            for h in purpose8:
                dynamoTable.put_item(
                    Item={
                        'id': str(uuid.uuid1()),
                        'firstname': first_name,
                        'lastname': last_name,
                        'email': email,
                        'gender': gender,
                        'address': address,
                        'referral': referral,
                        'timestamp': time,
                        'purpose': str(h),
                    }
                )
        messages.success(request, f'You have successfully checked in!')
        return redirect('user')

    return render(request, 'visitors/index.html', context={'form': form})

##First Form
def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            visitor = Visitor.objects.order_by()[len(Visitor.objects.order_by())-1]
            first_name = visitor.first_name
            last_name = visitor.last_name
            email = visitor.email

            purpose1 = visitor.purpose1
            purpose2 = visitor.purpose2
            purpose3 = visitor.purpose3
            purpose4 = visitor.purpose4
            purpose5 = visitor.purpose5
            purpose6 = visitor.purpose6
            purpose7 = visitor.purpose7
            purpose8 = visitor.purpose8

            currentDT = datetime.datetime.now()
            time = str(currentDT.strftime("%Y-%m-%d %I:%M:%S"))

            result = dynamoTable.scan()
            in_table = False
            for item in result['Items']:
                if item['firstname'] == first_name and item['lastname'] == last_name and item['email'] == email:
                    in_table = True
                    gender = item['gender']
                    referral = item['referral']
                    address = item['address']
                    break
            if in_table:
                for a in purpose1:
                    dynamoTable.put_item(
                        Item={
                            'id': str(uuid.uuid1()),
                            'firstname': first_name,
                            'lastname': last_name,
                            'email': email,
                            'gender': gender,
                            'address': address,
                            'referral': referral,
                            'timestamp': time,
                            'purpose': str(a),
                        }
                    )
                for b in purpose2:
                    dynamoTable.put_item(
                        Item={
                            'id': str(uuid.uuid1()),
                            'firstname': first_name,
                            'lastname': last_name,
                            'email': email,
                            'gender': gender,
                            'address': address,
                            'referral': referral,
                            'timestamp': time,
                            'purpose': str(b),
                        }
                    )
                for c in purpose3:
                    dynamoTable.put_item(
                        Item={
                            'id': str(uuid.uuid1()),
                            'firstname': first_name,
                            'lastname': last_name,
                            'email': email,
                            'gender': gender,
                            'address': address,
                            'referral': referral,
                            'timestamp': time,
                            'purpose': str(c),
                        }
                    )
                for d in purpose4:
                    dynamoTable.put_item(
                        Item={
                            'id': str(uuid.uuid1()),
                            'firstname': first_name,
                            'lastname': last_name,
                            'email': email,
                            'gender': gender,
                            'address': address,
                            'referral': referral,
                            'timestamp': time,
                            'purpose': str(d),
                        }
                    )
                for e in purpose5:
                    dynamoTable.put_item(
                        Item={
                            'id': str(uuid.uuid1()),
                            'firstname': first_name,
                            'lastname': last_name,
                            'email': email,
                            'gender': gender,
                            'address': address,
                            'referral': referral,
                            'timestamp': time,
                            'purpose': str(e),
                        }
                    )
                for f in purpose6:
                    dynamoTable.put_item(
                        Item={
                            'id': str(uuid.uuid1()),
                            'firstname': first_name,
                            'lastname': last_name,
                            'email': email,
                            'gender': gender,
                            'address': address,
                            'referral': referral,
                            'timestamp': time,
                            'purpose': str(f),
                        }
                    )
                for g in purpose7:
                    dynamoTable.put_item(
                        Item={
                            'id': str(uuid.uuid1()),
                            'firstname': first_name,
                            'lastname': last_name,
                            'email': email,
                            'gender': gender,
                            'address': address,
                            'referral': referral,
                            'timestamp': time,
                            'purpose': str(g),
                        }
                    )
                for h in purpose8:
                    dynamoTable.put_item(
                        Item={
                            'id': str(uuid.uuid1()),
                            'firstname': first_name,
                            'lastname': last_name,
                            'email': email,
                            'gender': gender,
                            'address': address,
                            'referral': referral,
                            'timestamp': time,
                            'purpose': str(h),
                        }
                    )
            else:
                request.session['first_name'], request.session['last_name'], request.session['email'], request.session['purpose1'], request.session['purpose2'], request.session['purpose3'], request.session['purpose4'], request.session['purpose5'], request.session['purpose6'], request.session['purpose7'], request.session['purpose8'],request.session['time'] = first_name, last_name, email, purpose1, purpose2, purpose3, purpose4, purpose5, purpose6, purpose7, purpose8, time
                return redirect('index')
        else:
            print('ERROR FORM INVALID')
        messages.success(request, f'You have successfully checked in!')
        return redirect('user')
    return render(request, 'visitors/users.html', {'form': form})
