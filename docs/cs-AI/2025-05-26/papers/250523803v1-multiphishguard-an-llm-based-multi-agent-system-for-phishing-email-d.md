---
layout: default
title: "MultiPhishGuard: An LLM-based Multi-Agent System for Phishing Email Detection"
---

# MultiPhishGuard: An LLM-based Multi-Agent System for Phishing Email Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23803" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23803v1</a>
  <a href="https://arxiv.org/pdf/2505.23803.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23803v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23803v1', 'MultiPhishGuard: An LLM-based Multi-Agent System for Phishing Email Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinuo Xue, Eric Spero, Yun Sing Koh, Giovanni Russello

**分类**: cs.CR, cs.AI

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出MultiPhishGuard以解决网络钓鱼邮件检测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络钓鱼` `邮件检测` `多代理系统` `对抗性学习` `强化学习` `安全防护` `可解释性`

## 📋 核心要点

1. 现有的网络钓鱼邮件检测方法面临对抗性策略不断演变的挑战，导致漏检和安全风险。
2. MultiPhishGuard通过动态多代理系统和对抗性强化学习，结合多个专业代理以提高检测效果。
3. 实验结果显示，MultiPhishGuard在准确率和假阳性、假阴性率方面均显著优于现有方法，提升效果明显。

## 📝 摘要（中文）

网络钓鱼邮件检测面临着不断演变的对抗性策略和异构攻击模式的重大挑战。传统的检测方法，如基于规则的过滤器和拒绝列表，往往难以跟上这些演变的策略，导致漏检和安全隐患。尽管机器学习方法提高了检测准确性，但在适应新型钓鱼策略方面仍面临挑战。本文提出了MultiPhishGuard，一个基于大型语言模型（LLM）的动态多代理检测系统，结合了专业知识与对抗性强化学习。该框架采用五个协作代理（文本、URL、元数据、解释简化器和对抗代理），通过近端策略优化算法自动调整决策权重。为应对新兴威胁，我们引入了对抗训练循环，生成微妙的上下文感知邮件变体，创建自我改善的防御生态系统，增强系统的鲁棒性。实验结果表明，MultiPhishGuard在公共数据集上显著优于现有的检测器，准确率达到97.89%，假阳性率为2.73%，假阴性率为0.20%。

## 🔬 方法详解

**问题定义**：本文旨在解决网络钓鱼邮件检测中的高漏检率和适应性不足的问题。现有的基于规则和机器学习的方法在面对不断演变的钓鱼策略时，往往无法有效应对，导致安全隐患。

**核心思路**：MultiPhishGuard的核心思路是通过构建一个动态的多代理系统，结合对抗性强化学习，利用多个代理的专业知识来提升检测的准确性和适应性。这样的设计使得系统能够实时调整决策权重，从而更好地应对新型钓鱼邮件。

**技术框架**：MultiPhishGuard的整体架构包括五个主要模块：文本代理、URL代理、元数据代理、解释简化器和对抗代理。每个代理负责不同的特征提取和决策过程，通过近端策略优化算法进行协作，形成一个自我改进的检测系统。

**关键创新**：本文的关键创新在于引入了对抗训练循环，通过对抗代理生成上下文感知的邮件变体，增强了系统的鲁棒性。这一方法与传统的静态检测方法有本质区别，能够动态适应新的攻击策略。

**关键设计**：在设计上，MultiPhishGuard采用了自动调整的决策权重机制，利用强化学习算法优化代理间的协作。此外，解释简化器的引入使得用户能够理解邮件分类的原因，提升了系统的可解释性。

## 📊 实验亮点

实验结果表明，MultiPhishGuard在公共数据集上的准确率高达97.89%，假阳性率仅为2.73%，假阴性率为0.20%。与现有的Chain-of-Thoughts和单代理基线相比，MultiPhishGuard显著提升了检测性能，验证了其在对抗性环境中的有效性。

## 🎯 应用场景

MultiPhishGuard在网络安全领域具有广泛的应用潜力，尤其是在企业和金融机构的邮件安全防护中。通过提高钓鱼邮件检测的准确性和适应性，该系统能够有效减少安全事件的发生，保护用户信息安全。未来，该技术还可以扩展到其他类型的网络攻击检测和防御中，提升整体网络安全水平。

## 📄 摘要（原文）

> Phishing email detection faces critical challenges from evolving adversarial tactics and heterogeneous attack patterns. Traditional detection methods, such as rule-based filters and denylists, often struggle to keep pace with these evolving tactics, leading to false negatives and compromised security. While machine learning approaches have improved detection accuracy, they still face challenges adapting to novel phishing strategies. We present MultiPhishGuard, a dynamic LLM-based multi-agent detection system that synergizes specialized expertise with adversarial-aware reinforcement learning. Our framework employs five cooperative agents (text, URL, metadata, explanation simplifier, and adversarial agents) with automatically adjusted decision weights powered by a Proximal Policy Optimization reinforcement learning algorithm. To address emerging threats, we introduce an adversarial training loop featuring an adversarial agent that generates subtle context-aware email variants, creating a self-improving defense ecosystem and enhancing system robustness. Experimental evaluations on public datasets demonstrate that MultiPhishGuard significantly outperforms Chain-of-Thoughts, single-agent baselines and state-of-the-art detectors, as validated by ablation studies and comparative analyses. Experiments demonstrate that MultiPhishGuard achieves high accuracy (97.89\%) with low false positive (2.73\%) and false negative rates (0.20\%). Additionally, we incorporate an explanation simplifier agent, which provides users with clear and easily understandable explanations for why an email is classified as phishing or legitimate. This work advances phishing defense through dynamic multi-agent collaboration and generative adversarial resilience.

