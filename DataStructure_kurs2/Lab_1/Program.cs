using System;
/*
 * Лабораторная 1 - реализовать три вида сортировки.
 */
namespace СSharpProject
{
    static class MainProgram
    {

        static void Main(string[] args)
        {
            Random rand = new Random();
            
            // Массив для первых двух заданий.
            int[] array_baza = new int[30];
            for (int i = 0; i < array_baza.Length; i++)
                array_baza[i] = rand.Next(-100, 100);
            
            
            // Массив для третьего задания (Задание 7).
            float[] array_variant = new float[30];
            for (int i = 0; i < array_variant.Length; i++){
                double temp = rand.NextDouble();
                temp = Math.Round(temp, 3);
                array_variant[i] = (float)temp;
            }
            
            Console.WriteLine("Массив для первых двух заданий:");
            Console.WriteLine("{0}", string.Join(" ", array_baza));
            Console.WriteLine();
            
            Console.WriteLine("Массив для третьего задания:");
            Console.WriteLine("{0}", string.Join(" ", array_variant));
            Console.WriteLine();
            Console.WriteLine();
            
            
            int[] QuickTest = array_baza;
            int[] CombTest = array_baza;

            
            Console.WriteLine("Быстрая сортировка: ");
            foreach (int i in QuickSort.Sort(QuickTest, 0, QuickTest.Length - 1))
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();
            Console.WriteLine();
            
            
            Console.WriteLine("Сортировка расчёской: ");
            foreach (int i in CombSort.Sort(CombTest))
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();
            Console.WriteLine();
            
            Console.WriteLine("Сортировка обменом/пузырьком: ");
            foreach (float i in BubbleSort.Sort(array_variant))
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();
            Console.WriteLine();
        }

        public static class QuickSort
        { // Быстрая сортировка
            public static int[] Sort(int[] input, int leftIndex, int rightIndex)
            {
                var i = leftIndex;
                var j = rightIndex;
                var pivot = input[leftIndex];

                while (i <= j)
                {
                    while (input[i] < pivot)
                    {
                        i++;
                    }

                    while (input[j] > pivot)
                    {
                        j--;
                    }

                    if (i <= j)
                    {
                        int temp = input[j];
                        input[j] = input[i];
                        input[i] = temp;
                        i++;
                        j--;

                    }
                }

                if (leftIndex < j)
                    Sort(input, leftIndex, j);
                if (i < rightIndex)
                    Sort(input, i, rightIndex);

                return input;
            }
        }

        public static class CombSort
        { // Сортировка расчёской
            public static int[] Sort(int[] input)
            {
                int gap = input.Length - 1;
                double div = 1.247;

                while (gap >= 1)
                {

                    for (int i = 0; i + gap < input.Length; i++)
                    {
                        if (input[i] > input[i + gap])
                        {
                            int temp = input[i + gap];
                            input[i + gap] = input[i];
                            input[i] = temp;
                        }
                    }

                    gap = Convert.ToInt32(Math.Truncate(gap / div));
                }
                return input;
            }
        }
        public static class BubbleSort
        { // Сортировка обменом/пузырьком.
            public static float[] Sort(float[] input)
            {
                for (int i = 0; i < input.Length; i++)
                {
                    for (int j = i + 1; j < input.Length; j++)
                    {
                        if (input[i] > input[j])
                        {
                            float temp = input[j];
                            input[j] = input[i];
                            input[i] = temp;
                        }
                    }
                }
                return input;
            }
        }
    }
}