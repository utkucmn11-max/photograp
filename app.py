
st.markdown("""
<style>

/* ELMAS KATMANI */
.diamond-bg {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    pointer-events: none;
    z-index: 1;
    overflow: hidden;
}

/* TEK ELMAS */
.diamond {
    position: absolute;
    width: 12px;
    height: 12px;
    background: rgba(0, 255, 255, 0.15);
    transform: rotate(45deg);
    animation: floatDiamond linear infinite;
    filter: blur(0.5px);
}

/* PARLAMA EFEKTİ */
.diamond::after {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(255,255,255,0.2);
    opacity: 0.3;
}

/* HAREKET */
@keyframes floatDiamond {
    0% {
        transform: translateY(100vh) rotate(45deg);
        opacity: 0;
    }
    10% {
        opacity: 0.4;
    }
    90% {
        opacity: 0.4;
    }
    100% {
        transform: translateY(-10vh) rotate(45deg);
        opacity: 0;
    }
}

</style>

<div class="diamond-bg">
""" + "".join([
    f'<div class="diamond" style="left:{i*5}%; animation-duration:{10 + i%10}s; animation-delay:{i*0.5}s;"></div>'
    for i in range(20)
]) + """
</div>
""", unsafe_allow_html=True)
