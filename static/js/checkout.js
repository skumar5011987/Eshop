$(document).ready(function () {
    $('.payWithRazorPay').click(function (e) {
        e.preventDefault();

        const fname = $('[name=fname]').val();
        const lname = $('[name=lname]').val();
        const email = $('[name=email]').val();
        const mobile = $('[name=mobile]').val();
        const address = $('[name=address]').val();
        const district = $('[name=district]').val();
        const state = $('[name=state]').val();
        const country = $('[name=country]').val();
        const pincode = $('[name=pincode]').val();
        const token = $("[name='csrfmiddlewaretoken']").val();

        if (fname == "" || lname == "" || email == "" || mobile == "" || address == "" || district == "" || state == "" ||
            country == "" || pincode == "") {
            swal("Alert!", "All fields are mendatory.", "error")
            return false;
        }
        else {
            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",
                success: function (response) {
                    // console.log(response)
                    var options = {
                        "key": "rzp_test_Mk9ESQ8qdMGUEs", // Enter the Key ID generated from the Dashboard
                        "amount": 1 * 100,//response.total_cost * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "E-shop",
                        "description": "Thank you for buying with us",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb) {
                            alert(responseb.razorpay_payment_id);
                            data = {
                                "fname": fname,
                                "lname": lname,
                                "email": email,
                                "mobile": mobile,
                                "address": address,
                                "district": district,
                                "state": state,
                                "country": country,
                                "pincode": pincode,
                                "payment_mode": 'Razorpay',
                                "payment_id": responseb.razorpay_payment_id,
                                csrfmiddlewaretoken: token

                            }
                            $.ajax({
                                method: "POST",
                                url: "/place-order",
                                data: data,
                                success: function (responsec) {
                                    swal("Congratulations!", responsec.status, "success").then((value) => {
                                        window.location.href = '/my-orders'
                                    });
                                }
                            });

                        },
                        "prefill": {
                            "name": fname + " " + lname,
                            "email": email,
                            "contact": mobile,
                        },
                        "theme": {
                            "color": "#195C61"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                }

            });
        }
    });
});