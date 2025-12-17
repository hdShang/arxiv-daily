---
layout: default
title: LightMem: Lightweight and Efficient Memory-Augmented Generation
---

# LightMem: Lightweight and Efficient Memory-Augmented Generation

**arXiv**: [2510.18866v1](https://arxiv.org/abs/2510.18866) | [PDF](https://arxiv.org/pdf/2510.18866.pdf)

**作者**: Jizhan Fang, Xinle Deng, Haoming Xu, Ziyan Jiang, Yuqi Tang, Ziwen Xu, Shumin Deng, Yunzhi Yao, Mengru Wang, Shuofei Qiao, Huajun Chen, Ningyu Zhang

---

## 💡 一句话要点

**提出LightMem以解决LLM在动态环境中高效利用历史交互信息的问题**

**关键词**: `大语言模型` `内存系统` `轻量压缩` `离线更新` `效率优化` `记忆机制`

## 📋 核心要点

1. LLM在动态复杂环境中难以有效利用历史交互信息，现有内存系统常引入高开销
2. LightMem基于人类记忆模型，分三阶段组织内存：感官、短时和长时记忆，实现轻量压缩与离线更新
3. 实验在LongMemEval上显示，准确率提升达10.9%，同时大幅减少token使用、API调用和运行时间

## 📄 摘要（原文）

> Despite their remarkable capabilities, Large Language Models (LLMs) struggle
> to effectively leverage historical interaction information in dynamic and
> complex environments. Memory systems enable LLMs to move beyond stateless
> interactions by introducing persistent information storage, retrieval, and
> utilization mechanisms. However, existing memory systems often introduce
> substantial time and computational overhead. To this end, we introduce a new
> memory system called LightMem, which strikes a balance between the performance
> and efficiency of memory systems. Inspired by the Atkinson-Shiffrin model of
> human memory, LightMem organizes memory into three complementary stages. First,
> cognition-inspired sensory memory rapidly filters irrelevant information
> through lightweight compression and groups information according to their
> topics. Next, topic-aware short-term memory consolidates these topic-based
> groups, organizing and summarizing content for more structured access. Finally,
> long-term memory with sleep-time update employs an offline procedure that
> decouples consolidation from online inference. Experiments on LongMemEval with
> GPT and Qwen backbones show that LightMem outperforms strong baselines in
> accuracy (up to 10.9% gains) while reducing token usage by up to 117x, API
> calls by up to 159x, and runtime by over 12x. The code is available at
> https://github.com/zjunlp/LightMem.

