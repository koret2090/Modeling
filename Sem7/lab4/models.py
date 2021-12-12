import random


def step_model(generator, processor, total_tasks=0, repeat=0, step=0.001):
    processed_tasks = 0
    t_curr = step
    t_gen_prev = t_proc = 0
    t_gen = generator.generate()
    t_proc = t_gen + processor.generate()
    cur_queue_len = max_queue_len = 0
    reentered_tasks = 0

    while processed_tasks < total_tasks:
        # Генератор
        if t_curr > t_gen:
            cur_queue_len += 1
            if cur_queue_len > max_queue_len:
                max_queue_len = cur_queue_len
            t_gen += generator.generate()

        # Обработчик
        if t_curr > t_proc:
            if cur_queue_len > 0:                
                processed_tasks += 1
                if random.randint(1, 100) <= repeat:
                    cur_queue_len += 1
                    reentered_tasks += 1
                cur_queue_len -= 1
                if cur_queue_len > 0:
                    t_proc += processor.generate()
                else:
                    t_proc = t_gen + processor.generate()
        t_curr += step

    return processed_tasks, reentered_tasks, max_queue_len, t_curr

def event_model(generator, processor, total_tasks=0, repeat=0):
    processed_tasks = 0
    t_gen = generator.generate()
    t_proc = t_gen + processor.generate()
    cur_queue_len = max_queue_len = 0
    reentered_tasks = 0
    while processed_tasks < total_tasks:
        # Генератор
        if t_gen <= t_proc:
            cur_queue_len += 1
            if cur_queue_len > max_queue_len:
                max_queue_len = cur_queue_len
            t_gen += generator.generate()

        # Обработчик
        if t_gen >= t_proc:
            if cur_queue_len > 0:                
                processed_tasks += 1
                if random.randint(1, 100) <= repeat:
                    cur_queue_len += 1
                    reentered_tasks += 1
                cur_queue_len -= 1
                if cur_queue_len > 0:
                    t_proc += processor.generate()
                else:
                    t_proc = t_gen + processor.generate()

    return processed_tasks, reentered_tasks, max_queue_len, t_proc