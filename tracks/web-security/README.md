# Web Security Track

## Safety Notice

Run web examples locally only. Never test third-party websites or applications without explicit written authorization.

## Topics

- HTTP requests and responses
- Cookies and sessions
- Input validation
- Authentication
- Authorization
- SQL and command injection concepts
- Security headers

## Local HTTP Example

Start a small server:

```bash
python3 -m http.server 8080
```

Then open `http://127.0.0.1:8080` and inspect:

```bash
curl -i http://127.0.0.1:8080/
```

## Questions

1. Which headers reveal server details?
2. Which headers improve browser security?
3. Why should an application validate input on the server?
4. How does authorization differ from authentication?
