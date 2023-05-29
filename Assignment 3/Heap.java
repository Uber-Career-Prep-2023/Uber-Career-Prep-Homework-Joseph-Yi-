import java.util.ArrayList;
import java.util.List;

public class Heap {
    private List<Integer> arr; // the underlying list

    public Heap() {
        arr = new ArrayList<>();
    }

    public int top() {
        if (arr.isEmpty()) {
            throw new IllegalStateException("Heap is empty");
        }
        return arr.get(0);
    }

    public void insert(int x) {
        arr.add(x);
        siftUp(arr.size() - 1);
    }

    public void remove() {
        if (arr.isEmpty()) {
            throw new IllegalStateException("Heap is empty");
        }
        swap(0, arr.size() - 1);
        arr.remove(arr.size() - 1);
        siftDown(0);
    }

    private void siftUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (arr.get(index) >= arr.get(parentIndex)) {
                break;
            }
            swap(index, parentIndex);
            index = parentIndex;
        }
    }

    private void siftDown(int index) {
        int size = arr.size();
        while (index < size) {
            int leftChildIndex = 2 * index + 1;
            int rightChildIndex = 2 * index + 2;
            int smallestChildIndex = index;

            if (leftChildIndex < size && arr.get(leftChildIndex) < arr.get(smallestChildIndex)) {
                smallestChildIndex = leftChildIndex;
            }

            if (rightChildIndex < size && arr.get(rightChildIndex) < arr.get(smallestChildIndex)) {
                smallestChildIndex = rightChildIndex;
            }

            if (smallestChildIndex == index) {
                break;
            }

            swap(index, smallestChildIndex);
            index = smallestChildIndex;
        }
    }

    private void swap(int i, int j) {
        int temp = arr.get(i);
        arr.set(i, arr.get(j));
        arr.set(j, temp);
    }
}
