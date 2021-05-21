FROM cdrx/pyinstaller-windows

COPY execute.sh /execute.sh
RUN chmod +x /execute.sh

ENTRYPOINT ["/execute.sh"]