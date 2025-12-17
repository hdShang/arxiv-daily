---
layout: default
title: TeleEgo: Benchmarking Egocentric AI Assistants in the Wild
---

# TeleEgo: Benchmarking Egocentric AI Assistants in the Wild

**arXiv**: [2510.23981v1](https://arxiv.org/abs/2510.23981) | [PDF](https://arxiv.org/pdf/2510.23981.pdf)

**作者**: Jiaqi Yan, Ruilong Ren, Jingren Liu, Shuning Xu, Ling Wang, Yiheng Wang, Yun Wang, Long Zhang, Xiangyu Chen, Changzhi Sun, Jixiang Luo, Dell Zhang, Hao Sun, Chi Zhang, Xuelong Li

---

## 💡 一句话要点

**提出TeleEgo基准以评估真实场景中的自我中心AI助手**

**关键词**: `自我中心AI助手` `多模态基准` `长期记忆评估` `流式处理` `真实场景数据集` `问答任务`

## 📋 核心要点

1. 现有基准缺乏多模态、流式、长期记忆的综合评估
2. 构建长时、流式、全模态数据集，涵盖工作、生活、社交等场景
3. 定义12个子任务和关键指标，评估记忆、理解和跨记忆推理能力

## 📄 摘要（原文）

> Egocentric AI assistants in real-world settings must process multi-modal
> inputs (video, audio, text), respond in real time, and retain evolving
> long-term memory. However, existing benchmarks typically evaluate these
> abilities in isolation, lack realistic streaming scenarios, or support only
> short-term tasks. We introduce \textbf{TeleEgo}, a long-duration, streaming,
> omni-modal benchmark for evaluating egocentric AI assistants in realistic daily
> contexts. The dataset features over 14 hours per participant of synchronized
> egocentric video, audio, and text across four domains: work \& study, lifestyle
> \& routines, social activities, and outings \& culture. All data is aligned on
> a unified global timeline and includes high-quality visual narrations and
> speech transcripts, curated through human refinement.TeleEgo defines 12
> diagnostic subtasks across three core capabilities: Memory (recalling past
> events), Understanding (interpreting the current moment), and Cross-Memory
> Reasoning (linking distant events). It contains 3,291 human-verified QA items
> spanning multiple question formats (single-choice, binary, multi-choice, and
> open-ended), evaluated strictly in a streaming setting. We propose two key
> metrics -- Real-Time Accuracy and Memory Persistence Time -- to jointly assess
> correctness, temporal responsiveness, and long-term retention. TeleEgo provides
> a realistic and comprehensive evaluation to advance the development of
> practical AI assistants.

