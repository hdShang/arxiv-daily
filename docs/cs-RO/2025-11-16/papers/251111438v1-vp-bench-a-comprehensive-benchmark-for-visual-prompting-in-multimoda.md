---
layout: default
title: VP-Bench: A Comprehensive Benchmark for Visual Prompting in Multimodal Large Language Models
---

# VP-Bench: A Comprehensive Benchmark for Visual Prompting in Multimodal Large Language Models

**arXiv**: [2511.11438v1](https://arxiv.org/abs/2511.11438) | [PDF](https://arxiv.org/pdf/2511.11438.pdf)

**作者**: Mingjie Xu, Jinpeng Chen, Yuzhi Zhao, Jason Chun Lok Li, Yue Qiu, Zekang Du, Mengyang Wu, Pingping Zhang, Kun Li, Hongzheng Yang, Wenao Ma, Jiaheng Wei, Qinbin Li, Kangcheng Liu, Wenqiang Lei

---

## 💡 一句话要点

**提出VP-Bench基准以评估多模态大语言模型在视觉提示理解与利用中的能力**

**关键词**: `多模态大语言模型` `视觉提示基准` `视觉语言理解` `模型评估` `下游任务应用`

## 📋 核心要点

1. 核心问题：现有基准缺乏对MLLMs解释视觉提示（如边界框）能力的系统评估
2. 方法要点：采用两阶段框架，评估视觉提示感知及其在下游任务中的影响
3. 实验或效果：评估28个MLLMs，分析视觉提示属性、问题安排和模型规模等因素

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have enabled a wide range of advanced vision-language applications, including fine-grained object recognition and contextual understanding. When querying specific regions or objects in an image, human users naturally use "visual prompts" (VPs), such as bounding boxes, to provide reference. However, no existing benchmark systematically evaluates the ability of MLLMs to interpret such VPs. This gap leaves it unclear whether current MLLMs can effectively recognize VPs, an intuitive prompting method for humans, and use them to solve problems. To address this limitation, we introduce VP-Bench, a benchmark for assessing MLLMs' capability in VP perception and utilization. VP-Bench employs a two-stage evaluation framework: Stage 1 examines models' ability to perceive VPs in natural scenes, using 30k visualized prompts spanning eight shapes and 355 attribute combinations. Stage 2 investigates the impact of VPs on downstream tasks, measuring their effectiveness in real-world problem-solving scenarios. Using VP-Bench, we evaluate 28 MLLMs, including proprietary systems (e.g., GPT-4o) and open-source models (e.g., InternVL3 and Qwen2.5-VL), and provide a comprehensive analysis of factors that affect VP understanding, such as variations in VP attributes, question arrangement, and model scale. VP-Bench establishes a new reference framework for studying how MLLMs comprehend and resolve grounded referring questions.

