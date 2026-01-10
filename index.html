<!DOCTYPE html>
<html>
<head>
    <title>DVC Intelligence Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
    <style>
        body { font-family: -apple-system, sans-serif; margin: 20px; background: #f8f9fa; color: #333; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .metric { font-size: 24px; font-weight: bold; color: #1a73e8; }
        .label { font-size: 14px; color: #666; text-transform: uppercase; margin-bottom: 10px; }
        .chart-container { background: white; padding: 20px; border-radius: 12px; margin-bottom: 20px; height: 350px; }
        table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #f1f3f4; }
        .badge-deal { background: #e6f4ea; color: #1e8e3e; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
        .badge-new { background: #e8f0fe; color: #1967d2; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>DVC Market Intelligence</h1>

    <div class="grid">
        <div class="card">
            <div class="label">Total Active Listings</div>
            <div id="totalListings" class="metric">--</div>
        </div>
        <div class="card">
            <div class="label">Avg Market Price</div>
            <div id="avgPrice" class="metric">--</div>
        </div>
        <div class="card">
            <div class="label">Top Value Resort</div>
            <div id="topValue" class="metric">--</div>
        </div>
    </div>

    <div class="grid">
        <div class="chart-container">
            <canvas id="inventoryChart"></canvas>
        </div>
        <div class="chart-container">
            <canvas id="priceDistChart"></canvas>
        </div>
    </div>

    <div class="card">
        <h2>Live Market Feed</h2>
        <table id="listingTable">
            <thead>
                <tr>
                    <th>Resort</th>
                    <th>Points</th>
                    <th>Price/Pt</th>
                    <th>Days on Market</th>
                    <th>Insight</th>
                </tr>
            </thead>
            <tbody id="listingBody"></tbody>
        </table>
    </div>

    <script>
        Papa.parse('data/listings_history.csv', {
            download: true, header: true,
            complete: function(results) {
                const data = results.data.filter(d => d.date);
                const dates = [...new Set(data.map(d => d.date))].sort();
                const latestDate = dates[dates.length - 1];
                const latestListings = data.filter(d => d.date === latestDate);

                // --- 1. METRICS ---
                document.getElementById('totalListings').innerText = latestListings.length;
                const avg = latestListings.reduce((s, c) => s + parseFloat(c.price_per_point.replace('$','')), 0) / latestListings.length;
                document.getElementById('avgPrice').innerText = `$${avg.toFixed(2)}`;

                // --- 2. INVENTORY VOLUME CHART ---
                const resorts = [...new Set(data.map(d => d.resort))].filter(r => r);
                new Chart(document.getElementById('inventoryChart'), {
                    type: 'line',
                    data: {
                        labels: dates,
                        datasets: resorts.map(r => ({
                            label: r,
                            data: dates.map(dt => data.filter(d => d.date === dt && d.resort === r).length),
                            fill: true, tension: 0.4
                        }))
                    },
                    options: { plugins: { title: { display: true, text: 'Inventory Volume by Resort' } }, scales: { y: { stacked: true } } }
                });

                // --- 3. PRICE DISTRIBUTION CHART ---
                const prices = latestListings.map(l => parseFloat(l.price_per_point.replace('$','')));
                new Chart(document.getElementById('priceDistChart'), {
                    type: 'bar',
                    data: {
                        labels: ['<$100', '$100-125', '$125-150', '$150-175', '>$175'],
                        datasets: [{
                            label: 'Number of Listings',
                            data: [
                                prices.filter(p => p < 100).length,
                                prices.filter(p => p >= 100 && p < 125).length,
                                prices.filter(p => p >= 125 && p < 150).length,
                                prices.filter(p => p >= 150 && p < 175).length,
                                prices.filter(p => p >= 175).length,
                            ],
                            backgroundColor: '#1a73e8'
                        }]
                    }
                });

                // --- 4. DAYS ON MARKET & TABLE ---
                const tableBody = document.getElementById('listingBody');
                latestListings.slice(0, 15).forEach(item => {
                    // Calculate "Days on Market" by counting how many dates this ID appears in
                    const daysOnMarket = data.filter(d => d.listing_id === item.listing_id).length;
                    const isNew = daysOnMarket === 1;
                    const priceNum = parseFloat(item.price_per_point.replace('$',''));
                    
                    let insight = isNew ? '<span class="badge-new">NEW</span>' : '';
                    if (priceNum < avg * 0.9) insight += ' <span class="badge-deal">🔥 UNDERVALUED</span>';

                    tableBody.innerHTML += `<tr>
                        <td>${item.resort}</td>
                        <td>${item.points}</td>
                        <td>${item.price_per_point}</td>
                        <td>${daysOnMarket} Day(s)</td>
                        <td>${insight}</td>
                    </tr>`;
                });
            }
        });
    </script>
</body>
</html>
