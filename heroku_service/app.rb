get '/' do
  "<b>Nylas webhooks interview question</b>
  <br><br>If you're seeing this, things have been installed correctly."
end


post '/webhook' do
  if rand(0..1) == 1 then
    [200, "Webhook processed!"]
  else
    [500, "Internal server error."]
  end
end
