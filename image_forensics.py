try:
    from PIL import Image # load the image
    from PIL.ExifTags import TAGS, GPSTAGS 
    
    import sys,os,json,time,pyfiglet
    from geopy.geocoders import Nominatim
    
except:
    raise ModuleNotFoundError

def image():
    if os.path.exists('E:\Final Year\Cyber\miniProject\Image\exif-samples\jpg\gps'):
        for images in os.listdir('E:\Final Year\Cyber\miniProject\Image\exif-samples\jpg\gps'):
            if images.endswith('.jpg'):
                check_exif(images)
            else:
                sys.exit('The image format must be jpg or jpeg')

def check_exif(picture):
    pics = Image.open(f'E:\Final Year\Cyber\miniProject\Image\exif-samples\jpg\gps\\{picture}')
    img_exif = pics.getexif()
    for _ in range(0,1):
        if img_exif is None:
            print("No EXIF in the picture!")
            print('\n')
            continue
        else:
            main(picture)
        
def convert_lat_long(degree:float, minutes:float,seconds:float):
    min = minutes/60.0
    sec  = seconds/3600.0
    return round(degree+min+sec,5)

def main(img_path):
    try:
        set = Image.open(f'E:\Final Year\Cyber\miniProject\Image\exif-samples\jpg\gps\\{img_path}')
        exifdata = set.getexif()
        for key,value in exifdata.items():
            decode = TAGS.get(key,key)
            data = exifdata.get(key)
            resultant = f'{decode:25} : {data}'
            print(resultant)
        print('\n')

        for indx, tag in TAGS.items():
            if tag == 'GPSInfo':
                if indx not in exifdata:
                    raise ValueError("No EXIF gps tag found")
                for key, val in GPSTAGS.items():
                    for key in exifdata[indx]:
                        gps_result = f"{val} : {exifdata[indx][key]}"
                        print(gps_result)
                latitude = list(exifdata[indx][2])
                longitude = list(exifdata[indx][4])

                lat = convert_lat_long(latitude[0],latitude[1],latitude[2])
                long = convert_lat_long(longitude[0],longitude[1],longitude[2])
                print(lat,long)
                geo = geolocation(lat,long)
                print("\n")
                print(f"Location Information: {geo}")
    
    except Exception as e:
        print(e)

def geolocation(latitude,longitude):
    geolocator = Nominatim(user_agent='metadata_extract')
    time.sleep(1)
    try:
        return geolocator.reverse(f"{latitude}-{longitude}").address
    except:
        return geolocation(latitude,longitude)

if __name__ == '__main__':
    x = image()
    print(x) 