function view_plot(value)
{
    switch(value)
    {
        case 'plot1': plot('http://127.0.0.1:8000/plot_1?start=1950&end=10&region=India', '(Plot-1)');break;
        case 'plot2': plot('http://127.0.0.1:8000/plot_2?start=1950&region_group=ASEAN', '(Plot-2)');break;
        case 'plot3': plot('http://127.0.0.1:8000/plot_3?start=1950&end=10&region_group=SAARC', '(Plot-3)');break;
        case 'plot4': plot('http://127.0.0.1:8000/plot_4?start=1950&region_group=ASEAN', '(Plot-4)');break;
    }
}

function plot(path, plot_number)
{
    fetch(path).then(response=>response.json()).then(
        data=>
          {
            Highcharts.chart('container', {
            chart: {
              type: 'column'
            },
            title: {
              text: data['title'],
              style:{fontSize:'30px',color:'darkred',fontWeight:'bold',textDecoration:'underline'}
            },
            subtitle: {
                text: plot_number,
                style:{fontSize:'15px',color:'blue',fontWeight:'bold'}
              },
            xAxis: {
              title: {
                text: data['x_axis_title'],
                style:{fontSize:'15px',color:'darkred',fontWeight:'bold'}
              },
              labels: {
                style: {
                  fontSize: "14px",
                  fontWeight:'bold',
                  color:'maroon'
                }
              },
              categories: data['x_axis_points'],
              crosshair: true 
            },
            yAxis: {
              min: 0,
              title: {
                text: data['y_axis_title'],
                style:{fontSize:'15px',color:'darkred',fontWeight:'bold'}
              },
              labels: {
                style: {
                  fontSize: "14px",
                  fontWeight:'bold',
                  color:'maroon'
                }
              }
            },
            tooltip: {
                headerFormat: '<span style="font-weight:bold;font-size:13px;">{point.key}</span><table>',
                pointFormat: '<tr><td style="font-size:16px;font-weight:bold;color:{series.color};padding:0">{series.name}: </td>' +
                  '<td style="padding:0"><b>{point.y:.0f} people</b></td></tr>',
                footerFormat: '</table>',
                shared: true,  
                useHTML: true  
              },
            plotOptions: {
              column: {
                pointPadding: 0.2,
                borderWidth: 0 
              }
            },
            series: data['plot_data']
          })
        
          if('start' in data)
          {
            document.getElementById('start').value=data['start'];
          }
          
          if('end' in data)
          {
            document.getElementById('end').value=data['end'];
          }

          if('region' in data)
          {
            document.getElementById('region').value=data['region'];
          }

          if('region_group' in data)
          {
            document.getElementById('region_group').value=data['region_group'];
          }
        
        });

        document.getElementById('which_plot').innerHTML=plot_number;
        
        if(plot_number=='(Plot-4)' || plot_number=='(Plot-2)' || plot_number=='(Plot-3)')
        {
          document.getElementById('region_group').style.display='inline';
          document.getElementById('region').style.display='none';
        }
        else
        {
          document.getElementById('region_group').style.display='none';
          document.getElementById('region').style.display='inline';
        }

        if(plot_number=='(Plot-4)' || plot_number=='(Plot-2)')
        {
          document.getElementById('range').style.display='none';
        }
        else
        {
          document.getElementById('range').style.display='inline';
        }

        if(plot_number=='(Plot-4)')
        {
          document.getElementById('start').max='2010';
        }
        else
        {
          document.getElementById('start').max='2015';
        }
}


function send_request()
{
  plot_number = document.getElementById("which_plot").innerHTML;
  
  if(plot_number == '(Plot-1)')
  {
    start = document.getElementById('start').value;
    end = document.getElementById('end').value;
    region = document.getElementById('region').value;
    path = 'http://127.0.0.1:8000/plot_1?start='+start+'&end='+end+'&region='+region;
    plot(path, plot_number);
  }

  if(plot_number == '(Plot-2)')
  {
    start = document.getElementById('start').value;
    region_group = document.getElementById('region_group').value;
    path = 'http://127.0.0.1:8000/plot_2?start='+start+'&region_group='+region_group;
    plot(path, plot_number);
  }

  if(plot_number == '(Plot-3)')
  {
    start = document.getElementById('start').value;
    end = document.getElementById('end').value;
    region_group = document.getElementById('region_group').value;
    path = 'http://127.0.0.1:8000/plot_3?start='+start+'&end='+end+'&region_group='+region_group;
    plot(path, plot_number);
  }

  if(plot_number == '(Plot-4)')
  {
    start = document.getElementById('start').value;
    region_group = document.getElementById('region_group').value;
    path = 'http://127.0.0.1:8000/plot_4?start='+start+'&region_group='+region_group;
    plot(path, plot_number);
  }
}