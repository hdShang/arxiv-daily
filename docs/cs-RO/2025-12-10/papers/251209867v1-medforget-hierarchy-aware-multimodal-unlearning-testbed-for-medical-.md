---
layout: default
title: MedForget: Hierarchy-Aware Multimodal Unlearning Testbed for Medical AI
---

# MedForget: Hierarchy-Aware Multimodal Unlearning Testbed for Medical AI

**arXiv**: [2512.09867v1](https://arxiv.org/abs/2512.09867) | [PDF](https://arxiv.org/pdf/2512.09867.pdf)

**作者**: Fengli Wu, Vaidehi Patil, Jaehong Yoon, Yue Zhang, Mohit Bansal

---

## 💡 一句话要点

**提出MedForget测试床以解决医疗AI中多模态大模型在隐私法规下的选择性遗忘问题**

**关键词**: `医疗AI` `多模态大模型` `选择性遗忘` `隐私合规` `层次感知评估` `重建攻击`

## 📋 核心要点

1. 核心问题：医疗AI中多模态大模型训练涉及敏感数据，需满足HIPAA/GDPR的遗忘权要求，但现有遗忘方法在复杂医疗场景中效果未知
2. 方法要点：构建层次感知多模态遗忘测试床，模拟医院数据嵌套层次，包含保留与遗忘分割及重述变体评估集
3. 实验或效果：在三个任务上测试四种SOTA遗忘方法，显示现有方法难以实现完全、层次感知的遗忘而不降低诊断性能

## 📄 摘要（原文）

> Pretrained Multimodal Large Language Models (MLLMs) are increasingly deployed in medical AI systems for clinical reasoning, diagnosis support, and report generation. However, their training on sensitive patient data raises critical privacy and compliance challenges under regulations such as HIPAA and GDPR, which enforce the "right to be forgotten". Unlearning, the process of tuning models to selectively remove the influence of specific training data points, offers a potential solution, yet its effectiveness in complex medical settings remains underexplored. To systematically study this, we introduce MedForget, a Hierarchy-Aware Multimodal Unlearning Testbed with explicit retain and forget splits and evaluation sets containing rephrased variants. MedForget models hospital data as a nested hierarchy (Institution -> Patient -> Study -> Section), enabling fine-grained assessment across eight organizational levels. The benchmark contains 3840 multimodal (image, question, answer) instances, each hierarchy level having a dedicated unlearning target, reflecting distinct unlearning challenges. Experiments with four SOTA unlearning methods on three tasks (generation, classification, cloze) show that existing methods struggle to achieve complete, hierarchy-aware forgetting without reducing diagnostic performance. To test whether unlearning truly deletes hierarchical pathways, we introduce a reconstruction attack that progressively adds hierarchical level context to prompts. Models unlearned at a coarse granularity show strong resistance, while fine-grained unlearning leaves models vulnerable to such reconstruction. MedForget provides a practical, HIPAA-aligned testbed for building compliant medical AI systems.

