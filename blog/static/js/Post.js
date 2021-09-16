import React from 'react';

class Post extends React.Component{
    render(){
        return(
            <div>
                <a href="{% url 'home' %}" id="post" > 戻る </a>
                <h1 id= 'title' >　　投稿フォーム</h1>
                <form action="{% url 'post' %}" method= "post" enctype="multipart/form-data">
                {% csrf_token %}
                {{ form.as_p }}
                <input type="submit" value= "送信" class="btn btn-info" />
                </form>
            </div>
        )
        
    }
}

export default Post;