---
layout: default
title: "We Politely Insist: Your LLM Must Learn the Persian Art of Taarof"
---

# We Politely Insist: Your LLM Must Learn the Persian Art of Taarof

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01035" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01035v1</a>
  <a href="https://arxiv.org/pdf/2509.01035.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01035v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01035v1', 'We Politely Insist: Your LLM Must Learn the Persian Art of Taarof')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikta Gohari Sadr, Sahar Heidariasl, Karine Megerdoomian, Laleh Seyyed-Kalantari, Ali Emami

**分类**: cs.CL

**发布日期**: 2025-09-01

**备注**: Accepted to EMNLP 2025 Main Conference

---

## 💡 一句话要点

**提出TaarofBench以解决大语言模型的文化理解问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `文化理解` `Taarof` `社交互动` `基准评估` `微调技术` `跨文化交流`

## 📋 核心要点

1. 现有的大语言模型在理解和应用文化特定的沟通规范方面存在显著不足，尤其是在波斯文化的Taarof礼仪中。
2. 论文提出了TaarofBench基准，通过450个角色扮演场景来评估LLM对Taarof的理解，填补了文化评估的空白。
3. 实验结果表明，LLM在文化适宜性方面的准确率低于母语者40-48%，通过微调技术实现了显著的性能提升。

## 📝 摘要（中文）

大语言模型（LLMs）在应对文化特定的沟通规范时面临挑战，限制了其在全球范围内的有效性。本文聚焦于波斯文化中的Taarof，这是一种强调尊重、谦逊和间接性的复杂礼仪规范，但在现有文化基准中缺失。我们引入了TaarofBench，这是第一个评估LLM对Taarof理解的基准，包含450个角色扮演场景，涵盖12个常见社交互动主题，并经过母语者验证。对五个前沿LLM的评估显示，在文化适宜的情况下，其准确率比母语者低40-48%。通过监督微调和直接偏好优化，我们在模型与文化期望的一致性上分别实现了21.8%和42.3%的提升。这项工作为开发多样化和文化敏感的LLM奠定了基础，使其能够更好地应对复杂的社交互动。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在理解和应用波斯文化中的Taarof礼仪时的不足，现有方法缺乏对文化特定沟通规范的有效评估。

**核心思路**：通过引入TaarofBench基准，提供一个系统化的评估框架，帮助LLM更好地理解和应用Taarof礼仪，提升其文化适应能力。

**技术框架**：整体架构包括数据收集、角色扮演场景设计、模型评估和优化四个主要模块。数据收集阶段通过母语者验证确保场景的真实性，评估阶段则使用多种LLM进行比较。

**关键创新**：TaarofBench是第一个专门针对波斯文化礼仪的评估基准，填补了现有文化评估工具的空白，且通过直接偏好优化显著提升了模型的文化适应性。

**关键设计**：在模型微调过程中，采用了监督学习和直接偏好优化的结合，设置了特定的损失函数以强化模型对Taarof礼仪的理解，确保模型输出符合文化期望。

## 📊 实验亮点

实验结果显示，五个前沿LLM在理解Taarof礼仪时的准确率比母语者低40-48%。通过监督微调和直接偏好优化，模型与文化期望的一致性分别提升了21.8%和42.3%，显示出显著的改进效果。

## 🎯 应用场景

该研究的潜在应用领域包括跨文化交流、社交机器人、智能客服等，能够帮助大语言模型更好地适应不同文化背景下的社交互动，提升用户体验。未来，这一研究可能推动多文化环境下的人工智能系统的发展，使其在全球化背景下更具有效性和适应性。

## 📄 摘要（原文）

> Large language models (LLMs) struggle to navigate culturally specific communication norms, limiting their effectiveness in global contexts. We focus on Persian taarof, a social norm in Iranian interactions, which is a sophisticated system of ritual politeness that emphasizes deference, modesty, and indirectness, yet remains absent from existing cultural benchmarks. We introduce TaarofBench, the first benchmark for evaluating LLM understanding of taarof, comprising 450 role-play scenarios covering 12 common social interaction topics, validated by native speakers. Our evaluation of five frontier LLMs reveals substantial gaps in cultural competence, with accuracy rates 40-48% below native speakers when taarof is culturally appropriate. Performance varies between interaction topics, improves with Persian-language prompts, and exhibits gender-based asymmetries. We also show that responses rated "polite" by standard metrics often violate taarof norms, indicating the limitations of Western politeness frameworks. Through supervised fine-tuning and Direct Preference Optimization, we achieve 21.8% and 42.3% improvement in model alignment with cultural expectations. Our human study with 33 participants (11 native Persian, 11 heritage, and 11 non-Iranian speakers) forms baselines in varying degrees of familiarity with Persian norms. This work lays the foundation for developing diverse and culturally aware LLMs, enabling applications that better navigate complex social interactions.

