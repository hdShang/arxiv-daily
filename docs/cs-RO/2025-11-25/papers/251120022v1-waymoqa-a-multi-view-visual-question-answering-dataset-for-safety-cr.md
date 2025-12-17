---
layout: default
title: WaymoQA: A Multi-View Visual Question Answering Dataset for Safety-Critical Reasoning in Autonomous Driving
---

# WaymoQA: A Multi-View Visual Question Answering Dataset for Safety-Critical Reasoning in Autonomous Driving

**arXiv**: [2511.20022v1](https://arxiv.org/abs/2511.20022) | [PDF](https://arxiv.org/pdf/2511.20022.pdf)

**作者**: Seungjun Yu, Seonho Lee, Namho Kim, Jaeyo Shin, Junsung Park, Wonjeong Ryu, Raehyuk Jung, Hyunjung Shim

---

## 💡 一句话要点

**提出WaymoQA数据集以解决自动驾驶中安全关键推理的挑战**

**关键词**: `自动驾驶` `安全关键推理` `多视图输入` `视觉问答数据集` `多模态大语言模型` `风险评估`

## 📋 核心要点

1. 核心问题：自动驾驶中安全关键场景的高层推理，避免一个风险可能引发另一个风险
2. 方法要点：利用多视图输入定义安全关键推理任务，并分解为两阶段处理
3. 实验或效果：微调后多模态大语言模型在安全关键场景推理能力显著提升

## 📄 摘要（原文）

> Recent advancements in multimodal large language models (MLLMs) have shown strong understanding of driving scenes, drawing interest in their application to autonomous driving. However, high-level reasoning in safety-critical scenarios, where avoiding one traffic risk can create another, remains a major challenge. Such reasoning is often infeasible with only a single front view and requires a comprehensive view of the environment, which we achieve through multi-view inputs. We define Safety-Critical Reasoning as a new task that leverages multi-view inputs to address this challenge. Then, we distill Safety-Critical Reasoning into two stages: first resolve the immediate risk, then mitigate the decision-induced downstream risks. To support this, we introduce WaymoQA, a dataset of 35,000 human-annotated question-answer pairs covering complex, high-risk driving scenarios. The dataset includes multiple-choice and open-ended formats across both image and video modalities. Experiments reveal that existing MLLMs underperform in safety-critical scenarios compared to normal scenes, but fine-tuning with WaymoQA significantly improves their reasoning ability, highlighting the effectiveness of our dataset in developing safer and more reasoning-capable driving agents.

