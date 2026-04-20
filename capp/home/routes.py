from flask import render_template, Blueprint
from capp.models import User, Transport

home = Blueprint("home", __name__)

@home.route("/")
@home.route("/home")
def home_home():
   
    user = User.query.filter_by(username="Bjørk").first()

    if not user:
        return render_template(
            "home.html",
            user_name="Bjørk",
            user_transports=[],
            kms=None,
            max_kms=None,
            co2=None,
            co2_kms=None,
            max_co2_kms=None,
            transport_type=None,
            transport_max_co2_kms=None,
        )

    user_transports = Transport.query.filter_by(user_id=user.id).all()

    first_transport = user_transports[0] if user_transports else None

    
    kms = round(first_transport.kms, 2) if first_transport and first_transport.kms is not None else None

 
    max_kms = max((t.kms for t in user_transports if t.kms is not None), default=None)

    
    co2 = round(first_transport.co2, 2) if first_transport and first_transport.co2 is not None else None
    co2_kms = (
        round(first_transport.co2 / first_transport.kms, 2)
        if first_transport
        and first_transport.co2 is not None
        and first_transport.kms not in (None, 0)
        else None
    )

   
    valid_transports = [
        t for t in user_transports
        if t.co2 is not None and t.kms not in (None, 0)
    ]

    transport_with_max_co2_kms = (
        max(valid_transports, key=lambda t: t.co2 / t.kms)
        if valid_transports else None
    )

    max_co2_kms = (
        round(transport_with_max_co2_kms.co2 / transport_with_max_co2_kms.kms, 2)
        if transport_with_max_co2_kms else None
    )

    transport_type = (
        transport_with_max_co2_kms.transport
        if transport_with_max_co2_kms else None
    )

    transport_max_co2_kms = max_co2_kms

    return render_template(
        "home.html",
        user_name=user.username,
        user_transports=user_transports,
        kms=kms,
        max_kms=max_kms,
        co2=co2,
        co2_kms=co2_kms,
        max_co2_kms=max_co2_kms,
        transport_type=transport_type,
        transport_max_co2_kms=transport_max_co2_kms,
    )

