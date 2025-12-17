---
layout: default
title: Cook and Clean Together: Teaching Embodied Agents for Parallel Task Execution
---

# Cook and Clean Together: Teaching Embodied Agents for Parallel Task Execution

**arXiv**: [2511.19430v1](https://arxiv.org/abs/2511.19430) | [PDF](https://arxiv.org/pdf/2511.19430.pdf)

**作者**: Dingkang Liang, Cheng Zhang, Xiaopeng Xu, Jianzhong Ju, Zhenbo Luo, Xiang Bai

---

## 💡 一句话要点

**提出ORS3D任务与GRANT模型，以优化具身AI在3D环境中的并行任务调度效率**

**关键词**: `具身AI` `任务调度` `3D基础` `运筹学` `多模态大语言模型` `并行执行`

## 📋 核心要点

1. 核心问题：现有数据集忽略运筹学知识与3D空间基础，限制具身AI任务调度效率
2. 方法要点：构建ORS3D-60K数据集，并开发GRANT模型，集成调度令牌机制生成高效计划
3. 实验或效果：在ORS3D-60K上验证GRANT在语言理解、3D基础与调度效率的有效性

## 📄 摘要（原文）

> Task scheduling is critical for embodied AI, enabling agents to follow natural language instructions and execute actions efficiently in 3D physical worlds. However, existing datasets often simplify task planning by ignoring operations research (OR) knowledge and 3D spatial grounding. In this work, we propose Operations Research knowledge-based 3D Grounded Task Scheduling (ORS3D), a new task that requires the synergy of language understanding, 3D grounding, and efficiency optimization. Unlike prior settings, ORS3D demands that agents minimize total completion time by leveraging parallelizable subtasks, e.g., cleaning the sink while the microwave operates. To facilitate research on ORS3D, we construct ORS3D-60K, a large-scale dataset comprising 60K composite tasks across 4K real-world scenes. Furthermore, we propose GRANT, an embodied multi-modal large language model equipped with a simple yet effective scheduling token mechanism to generate efficient task schedules and grounded actions. Extensive experiments on ORS3D-60K validate the effectiveness of GRANT across language understanding, 3D grounding, and scheduling efficiency. The code is available at https://github.com/H-EmbodVis/GRANT

