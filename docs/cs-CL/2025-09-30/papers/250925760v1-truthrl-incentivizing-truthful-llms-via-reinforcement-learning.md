---
layout: default
title: "TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning"
---

# TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25760" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25760v1</a>
  <a href="https://arxiv.org/pdf/2509.25760.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25760v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25760v1', 'TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhepei Wei, Xiao Yang, Kai Sun, Jiaqi Wang, Rulin Shao, Sean Chen, Mohammad Kachuee, Teja Gollapudi, Tony Liao, Nicolas Scheffer, Rakesh Wanga, Anuj Kumar, Yu Meng, Wen-tau Yih, Xin Luna Dong

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**TruthRL：通过强化学习激励大型语言模型生成更真实可靠的答案**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `真实性` `幻觉` `知识密集型问答` `三元奖励` `GRPO`

## 📋 核心要点

1. 现有大型语言模型在知识密集型任务中易产生幻觉，且难以平衡准确性和识别不确定性。
2. TruthRL通过强化学习框架，使用三元奖励（正确、幻觉、弃权）直接优化模型的真实性。
3. 实验表明，TruthRL显著降低了幻觉率（28.9%）并提升了真实性（21.1%），优于传统强化学习方法。

## 📝 摘要（中文）

大型语言模型（LLMs）在事实性问答方面表现出色，但容易产生幻觉和不真实的回答，尤其是在需要超出其参数知识的信息时。真实性不仅仅是准确性，模型还必须识别不确定性并在不确定时选择弃权以避免幻觉。现有方法面临根本挑战：优化准确性的方法通常会放大幻觉，而鼓励弃权的方法可能过于保守，牺牲了正确的答案。本文提出了TruthRL，一个通用的强化学习（RL）框架，直接优化LLM的真实性。TruthRL使用GRPO实现，采用简单而有效的三元奖励，区分正确答案、幻觉和弃权。它激励模型通过提供正确答案和在不确定时选择弃权来减少幻觉，从而提高真实性。在四个知识密集型基准测试中，与vanilla RL相比，TruthRL显著减少了28.9%的幻觉，提高了21.1%的真实性，在检索和非检索设置下，各种骨干模型（例如，Qwen、Llama）都获得了持续的收益。深入的消融研究表明，vanilla的以准确性驱动的方法，例如监督微调或具有二元奖励的RL，难以平衡事实正确性和不确定性。相比之下，我们提出的以真实性驱动的TruthRL在准确性和真实性方面都取得了出色的性能，突出了学习目标设计对于开发真实的LLM的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在知识密集型问答任务中存在的幻觉问题，即模型在缺乏足够信息的情况下，生成不真实或不准确的答案。现有方法，如监督微调或使用二元奖励的强化学习，难以在追求准确性的同时，有效识别和处理自身的不确定性，导致模型要么过度自信地产生幻觉，要么过于保守地放弃回答。

**核心思路**：TruthRL的核心思路是通过强化学习直接优化模型的真实性，而不仅仅是准确性。它通过引入一个三元奖励函数，明确区分正确答案、幻觉和弃权，从而激励模型在不确定时选择弃权，避免产生幻觉。这种方法旨在使模型能够更好地校准其置信度，并在知识边界之外表现出适当的谦逊。

**技术框架**：TruthRL使用GRPO（Generalized Proximal Policy Optimization）作为强化学习算法。整体流程如下：1) 使用LLM生成答案；2) 根据答案的事实性给予三元奖励（正确、幻觉、弃权）；3) 使用GRPO更新LLM的策略，使其更倾向于生成真实答案或在不确定时选择弃权。该框架可以应用于各种LLM，并且可以与检索增强方法结合使用。

**关键创新**：TruthRL的关键创新在于其三元奖励函数，它明确区分了正确答案、幻觉和弃权。与传统的二元奖励（正确/错误）相比，三元奖励能够更细致地指导模型的学习，使其不仅关注生成正确答案，还关注识别和避免幻觉。这种奖励机制鼓励模型在不确定时选择弃权，从而提高整体的真实性。

**关键设计**：TruthRL使用GRPO算法进行策略优化。三元奖励函数的设计是关键，具体数值可以根据任务和模型进行调整。例如，正确答案奖励为+1，幻觉奖励为-1，弃权奖励为0。此外，论文还研究了不同的弃权策略，例如基于模型置信度的弃权。具体的网络结构取决于所使用的LLM。

## 📊 实验亮点

实验结果表明，TruthRL在四个知识密集型基准测试中，与vanilla RL相比，显著减少了28.9%的幻觉，提高了21.1%的真实性。在Qwen和Llama等不同骨干模型上，以及在检索和非检索设置下，TruthRL都表现出一致的性能提升。消融研究表明，三元奖励函数是TruthRL成功的关键，优于传统的二元奖励方法。

## 🎯 应用场景

TruthRL可应用于各种需要高度可靠性的知识密集型问答场景，例如医疗诊断、金融分析、法律咨询等。通过提高LLM的真实性，可以减少错误信息的传播，增强用户对AI系统的信任，并促进AI在关键领域的应用。未来，该方法可以扩展到其他类型的生成任务，例如文本摘要和机器翻译。

## 📄 摘要（原文）

> While large language models (LLMs) have demonstrated strong performance on factoid question answering, they are still prone to hallucination and untruthful responses, particularly when tasks demand information outside their parametric knowledge. Indeed, truthfulness requires more than accuracy -- models must also recognize uncertainty and abstain when unsure to avoid hallucinations. This presents a fundamental challenge for existing methods: approaches that optimize for accuracy often amplify hallucinations, while those that encourage abstention can become overly conservative, sacrificing correct answers. Both extremes ultimately compromise truthfulness. In this work, we present TruthRL, a general reinforcement learning (RL) framework that directly optimizes the truthfulness of LLMs. Specifically, we implement TruthRL using GRPO with a simple yet effective ternary reward that distinguishes correct answers, hallucinations, and abstentions. It incentivizes models to reduce hallucinations not only by providing correct responses, but also by enabling abstention when uncertain, thereby improving truthfulness. Extensive experiments across four knowledge-intensive benchmarks show that, compared to vanilla RL, TruthRL significantly reduces hallucinations by 28.9% and improves truthfulness by 21.1%, with consistent gains across various backbone models (e.g., Qwen, Llama) under both retrieval and non-retrieval setups. In-depth ablation study demonstrates that vanilla accuracy-driven methods, such as supervised fine-tuning or RL with a binary reward, struggle to balance factual correctness and uncertainty. In contrast, our proposed truthfulness-driven TruthRL achieves strong performance in both accuracy and truthfulness, underscoring the importance of learning objective design for developing truthful LLMs.

