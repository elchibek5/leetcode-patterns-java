// LeetCode's NestedInteger interface (339, 341, 364, 385).
import java.util.List;

public interface NestedInteger {
    boolean isInteger();
    Integer getInteger();
    void setInteger(int value);
    void add(NestedInteger ni);
    List<NestedInteger> getList();
}
