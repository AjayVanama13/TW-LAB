def dot_product(vec1,vec2):
    if len(vec1)!=len(vec2):
        raise ValueError("should be same length")
        result=sum(v1*v2 for v1,v2 in zip(vec1,vec2))
        return result