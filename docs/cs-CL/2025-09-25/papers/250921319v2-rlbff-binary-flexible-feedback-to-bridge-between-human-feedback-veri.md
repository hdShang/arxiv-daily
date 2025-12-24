---
layout: default
title: "RLBFF: Binary Flexible Feedback to bridge between Human Feedback & Verifiable Rewards"
---

# RLBFF: Binary Flexible Feedback to bridge between Human Feedback & Verifiable Rewards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21319" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21319v2</a>
  <a href="https://arxiv.org/pdf/2509.21319.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21319v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21319v2', 'RLBFF: Binary Flexible Feedback to bridge between Human Feedback & Verifiable Rewards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhilin Wang, Jiaqi Zeng, Olivier Delalleau, Ellie Evans, Daniel Egert, Hoo-Chang Shin, Felipe Soares, Yi Dong, Oleksii Kuchaiev

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-25 (更新: 2025-10-30)

**备注**: Added link to access models: https://huggingface.co/collections/nvidia/reward-models-10-2025

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/collections/nvidia)

---

## 💡 一句话要点

**提出RLBFF，结合人类反馈和可验证奖励，提升LLM对齐效果并支持推理时自定义原则。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `人类反馈` `奖励模型` `大语言模型对齐` `二元反馈`

## 📋 核心要点

1. RLHF依赖人类反馈，缺乏明确标准，导致可解释性差和易受奖励操纵；RLVR则受限于基于正确性的验证器，适用范围有限。
2. RLBFF从人类反馈中提取二元原则，将奖励模型训练转化为蕴含任务，从而结合了人类反馈的灵活性和规则验证的精确性。
3. 实验表明，RLBFF训练的奖励模型在RM-Bench和JudgeBench上取得了领先性能，并能以低成本对齐Qwen3-32B，媲美更大型的模型。

## 📝 摘要（中文）

本文提出了一种新的强化学习范式：基于二元灵活反馈的强化学习（RLBFF），旨在结合人类反馈（RLHF）和可验证奖励（RLVR）的优势。RLHF依赖人类判断，缺乏可解释性和易受奖励操纵，而RLVR则受限于基于正确性的验证器。RLBFF从自然语言反馈中提取可以用二元方式回答的原则（例如，信息准确性：是/否，代码可读性：是/否）。这些原则可用于将奖励模型的训练转化为蕴含任务（response是否满足特定原则）。实验表明，在这种方式下训练的奖励模型在数据匹配时优于Bradley-Terry模型，并在RM-Bench（86.2%）和JudgeBench（81.4%，截至2025年9月24日排名第一）上取得了最佳性能。此外，用户可以在推理时指定感兴趣的原则，从而定制奖励模型的关注点。最后，本文提供了一个完全开源的方案（包括数据），使用RLBFF和我们的奖励模型对Qwen3-32B进行对齐，在MT-Bench、WildBench和Arena Hard v2等通用对齐基准测试中，达到或超过o3-mini和DeepSeek R1的性能（且推理成本低于5%）。

## 🔬 方法详解

**问题定义**：现有的大语言模型对齐方法，如RLHF和RLVR，各有不足。RLHF依赖于主观的人类反馈，缺乏明确的评判标准，导致奖励模型难以解释，容易被模型“奖励攻击”。RLVR虽然有明确的规则，但只能针对特定类型的任务（如代码生成）进行验证，难以泛化到更广泛的场景。因此，需要一种既能利用人类反馈的灵活性，又能保证奖励信号可解释性的方法。

**核心思路**：RLBFF的核心思路是从自然语言形式的人类反馈中提取出可以用二元形式（是/否）回答的原则。例如，对于一个文本生成任务，可以提取出“信息是否准确”、“语言是否流畅”等原则。然后，将奖励模型的训练转化为一个蕴含任务：判断生成的文本是否满足这些原则。这样，奖励模型不仅可以学习人类的偏好，还可以学习到明确的评判标准。

**技术框架**：RLBFF的整体框架包括以下几个主要步骤：1) 收集包含自然语言反馈的数据集；2) 从自然语言反馈中提取二元原则；3) 使用提取的原则训练奖励模型，将训练目标设定为判断生成文本是否满足这些原则的蕴含任务；4) 使用训练好的奖励模型进行强化学习，对大语言模型进行对齐。

**关键创新**：RLBFF最重要的创新点在于将自然语言反馈转化为二元原则，从而将奖励模型的训练转化为一个蕴含任务。这种方法既利用了人类反馈的灵活性，又保证了奖励信号的可解释性。此外，RLBFF还允许用户在推理时指定感兴趣的原则，从而定制奖励模型的行为。

**关键设计**：RLBFF的关键设计包括：1) 如何从自然语言反馈中有效地提取二元原则（具体方法未知，论文中可能未详细说明）；2) 如何设计蕴含任务的损失函数，使得奖励模型能够准确地判断生成文本是否满足特定原则；3) 如何将奖励模型与强化学习算法相结合，有效地对大语言模型进行对齐。具体参数设置和网络结构等细节在论文中可能有所描述，但此处无法详细展开。

## 📊 实验亮点

实验结果表明，RLBFF训练的奖励模型在RM-Bench上达到了86.2%的准确率，在JudgeBench上达到了81.4%的准确率（截至2025年9月24日排名第一）。此外，使用RLBFF对齐的Qwen3-32B模型在MT-Bench、WildBench和Arena Hard v2等通用对齐基准测试中，达到了或超过了o3-mini和DeepSeek R1的性能，且推理成本低于5%。这些结果表明，RLBFF是一种有效的模型对齐方法。

## 🎯 应用场景

RLBFF可应用于各种需要人类反馈的大语言模型对齐场景，例如文本生成、代码生成、对话系统等。通过提取二元原则，RLBFF可以提高奖励模型的可解释性和鲁棒性，降低奖励攻击的风险。此外，RLBFF还支持用户自定义原则，从而实现个性化的模型对齐。该研究有望推动大语言模型在实际应用中的广泛部署。

## 📄 摘要（原文）

> Reinforcement Learning with Human Feedback (RLHF) and Reinforcement Learning with Verifiable Rewards (RLVR) are the main RL paradigms used in LLM post-training, each offering distinct advantages. However, RLHF struggles with interpretability and reward hacking because it relies on human judgments that usually lack explicit criteria, whereas RLVR is limited in scope by its focus on correctness-based verifiers. We propose Reinforcement Learning with Binary Flexible Feedback (RLBFF), which combines the versatility of human-driven preferences with the precision of rule-based verification, enabling reward models to capture nuanced aspects of response quality beyond mere correctness. RLBFF extracts principles that can be answered in a binary fashion (e.g. accuracy of information: yes, or code readability: no) from natural language feedback. Such principles can then be used to ground Reward Model training as an entailment task (response satisfies or does not satisfy an arbitrary principle). We show that Reward Models trained in this manner can outperform Bradley-Terry models when matched for data and achieve top performance on RM-Bench (86.2%) and JudgeBench (81.4%, #1 on leaderboard as of September 24, 2025). Additionally, users can specify principles of interest at inference time to customize the focus of our reward models, in contrast to Bradley-Terry models. Finally, we present a fully open source recipe (including data) to align Qwen3-32B using RLBFF and our Reward Model, to match or exceed the performance of o3-mini and DeepSeek R1 on general alignment benchmarks of MT-Bench, WildBench, and Arena Hard v2 (at <5% of the inference cost). Models: https://huggingface.co/collections/nvidia/reward-models-10-2025

