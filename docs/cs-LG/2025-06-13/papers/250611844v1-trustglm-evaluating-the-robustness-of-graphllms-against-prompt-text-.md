---
layout: default
title: "TrustGLM: Evaluating the Robustness of GraphLLMs Against Prompt, Text, and Structure Attacks"
---

# TrustGLM: Evaluating the Robustness of GraphLLMs Against Prompt, Text, and Structure Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11844" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11844v1</a>
  <a href="https://arxiv.org/pdf/2506.11844.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11844v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11844v1', 'TrustGLM: Evaluating the Robustness of GraphLLMs Against Prompt, Text, and Structure Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qihai Zhang, Xinyue Sheng, Yuanfu Sun, Qiaoyu Tan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-13

**备注**: 12 pages, 5 figures, in KDD 2025

---

## 💡 一句话要点

**提出TrustGLM以评估GraphLLMs对对抗性攻击的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图学习` `对抗性攻击` `鲁棒性评估` `大型语言模型` `防御技术` `数据增强` `对抗训练`

## 📋 核心要点

1. 现有GraphLLMs在对抗性攻击下的鲁棒性研究不足，限制了其在高风险场景中的应用。
2. 提出TrustGLM，通过评估GraphLLMs在文本、图结构和提示操控等方面的脆弱性，填补这一研究空白。
3. 实验结果表明，GraphLLMs对文本和结构攻击高度敏感，且通过数据增强和对抗训练可显著提升模型鲁棒性。

## 📝 摘要（中文）

受大型语言模型（LLMs）成功的启发，研究者们从传统图学习方法转向基于LLM的图框架，称为GraphLLMs。尽管GraphLLMs展现出强大的推理能力，但其在对抗性扰动下的鲁棒性尚未得到充分探讨。为此，我们提出了TrustGLM，全面评估GraphLLMs在文本、图结构和提示操控等三个维度上的脆弱性。通过在六个基准数据集上的广泛实验，我们发现GraphLLMs对文本攻击高度敏感，标准图结构攻击方法显著降低模型性能，而提示模板中的候选标签集随机打乱也会导致性能大幅下降。我们还探讨了针对每种攻击向量的防御技术，显示出增强GraphLLMs鲁棒性的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决GraphLLMs在面对对抗性攻击时的脆弱性问题。现有方法未能充分评估其在文本、图结构和提示操控等方面的鲁棒性，导致在实际应用中存在潜在风险。

**核心思路**：通过引入TrustGLM，系统性地评估GraphLLMs在不同攻击向量下的表现，旨在揭示其脆弱性并探索有效的防御策略。此设计旨在为GraphLLMs的安全性提供理论基础和实践指导。

**技术框架**：TrustGLM的整体架构包括三个主要模块：文本攻击、图结构攻击和提示操控攻击。每个模块采用先进的攻击算法进行评估，并结合数据增强和对抗训练进行防御策略的探索。

**关键创新**：本研究的主要创新在于系统性地评估GraphLLMs的脆弱性，尤其是在文本攻击和结构攻击方面的发现，揭示了这些模型在实际应用中的潜在风险。与现有方法相比，TrustGLM提供了更全面的评估框架。

**关键设计**：在实验中，采用了多种攻击算法，并通过数据增强和对抗训练来提升模型的鲁棒性。具体的参数设置和损失函数设计经过多次实验验证，以确保防御策略的有效性。

## 📊 实验亮点

实验结果显示，GraphLLMs对文本攻击的敏感性极高，仅用少量语义相似的词替换就能显著降低性能。此外，标准图结构攻击方法导致模型性能下降，而提示模板中候选标签集的随机打乱也造成了显著的性能下降。通过对抗训练和数据增强，模型鲁棒性得到了有效提升。

## 🎯 应用场景

该研究的潜在应用领域包括社交网络分析、推荐系统和金融欺诈检测等高风险场景。通过提升GraphLLMs的鲁棒性，可以增强这些系统在面对对抗性攻击时的安全性，从而提高其在实际应用中的可靠性和有效性。未来，TrustGLM的研究成果有望推动更多创新的防御技术的发展。

## 📄 摘要（原文）

> Inspired by the success of large language models (LLMs), there is a significant research shift from traditional graph learning methods to LLM-based graph frameworks, formally known as GraphLLMs. GraphLLMs leverage the reasoning power of LLMs by integrating three key components: the textual attributes of input nodes, the structural information of node neighborhoods, and task-specific prompts that guide decision-making. Despite their promise, the robustness of GraphLLMs against adversarial perturbations remains largely unexplored-a critical concern for deploying these models in high-stakes scenarios. To bridge the gap, we introduce TrustGLM, a comprehensive study evaluating the vulnerability of GraphLLMs to adversarial attacks across three dimensions: text, graph structure, and prompt manipulations. We implement state-of-the-art attack algorithms from each perspective to rigorously assess model resilience. Through extensive experiments on six benchmark datasets from diverse domains, our findings reveal that GraphLLMs are highly susceptible to text attacks that merely replace a few semantically similar words in a node's textual attribute. We also find that standard graph structure attack methods can significantly degrade model performance, while random shuffling of the candidate label set in prompt templates leads to substantial performance drops. Beyond characterizing these vulnerabilities, we investigate defense techniques tailored to each attack vector through data-augmented training and adversarial training, which show promising potential to enhance the robustness of GraphLLMs. We hope that our open-sourced library will facilitate rapid, equitable evaluation and inspire further innovative research in this field.

