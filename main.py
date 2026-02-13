from workers import Response, WorkerEntrypoint

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        # Handle GET: Show the Workshop Form
        if request.method == "GET":
            html = """
            <!DOCTYPE html>
            <html>
            <head><title>CUPP Web</title></head>
            <body style="font-family:sans-serif; padding:40px;">
                <h2>Target Profiler (Workshop Tool)</h2>
                <form method="POST">
                    <input name="fname" placeholder="First Name" required><br><br>
                    <input name="pet" placeholder="Pet Name"><br><br>
                    <input name="year" placeholder="Birth Year"><br><br>
                    <button type="submit">Generate Wordlist</button>
                </form>
            </body>
            </html>
            """
            return Response(html, headers={"Content-Type": "text/html"})

        # Handle POST: Generate Passwords
        if request.method == "POST":
            # In Python Workers, we use await request.form_data()
            form = await request.form_data()
            fname = str(form.get("fname") or "").lower()
            pet = str(form.get("pet") or "").lower()
            year = str(form.get("year") or "")

            results = {fname, f"{fname}123", f"{fname}{year}"}
            if pet:
                results.update({pet, f"{pet}123", f"{pet}{year}", f"{pet}!"})
            
            # Add a 'Secret' password for your challenge here if you want
            results.add("ChallengeWinner2026!") 

            return Response("\\n".join(sorted(results)), headers={"Content-Type": "text/plain"})
