---
layout: default
title: Masked IRL: LLM-Guided Reward Disambiguation from Demonstrations and Language
---

# Masked IRL: LLM-Guided Reward Disambiguation from Demonstrations and Language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14565" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14565v1</a>
  <a href="https://arxiv.org/pdf/2511.14565.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14565v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14565v1', 'Masked IRL: LLM-Guided Reward Disambiguation from Demonstrations and Language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minyoung Hwang, Alexandra Forsey-Smerek, Nathaniel Dennler, Andreea Bobu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-18

**🔗 代码/项目**: [GITHUB](https://github.com/MIT-CLEAR-Lab/Masked-IRL) | [PROJECT_PAGE](https://MIT-CLEAR-Lab.github.io/Masked-IRL)

---

## 💡 一句话要点

**提出Masked IRL以解决机器人奖励函数模糊问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `逆强化学习` `大语言模型` `机器人学习` `奖励函数` `模糊指令` `样本效率` `人机交互`

## 📋 核心要点

1. 现有的奖励学习方法在数据有限时容易过拟合，导致模型无法有效泛化，尤其是在处理模糊指令时。
2. Masked IRL框架结合了示范和语言指令的优势，通过推断状态相关性掩码来增强模型的鲁棒性。
3. 实验结果表明，Masked IRL在使用数据量减少的情况下，性能提升可达15%，显示出更高的样本效率和泛化能力。

## 📝 摘要（中文）

机器人可以通过示范学习用户偏好的奖励函数，但在数据有限的情况下，奖励模型往往会过拟合于虚假相关性，导致泛化能力不足。现有方法通常将语言指令视为简单的条件信号，未能充分利用其消除模糊性的潜力。本文提出Masked Inverse Reinforcement Learning (Masked IRL)框架，结合大语言模型（LLMs）和示范数据，推断状态相关性掩码，从而增强模型对无关状态组件的鲁棒性。在模拟和真实机器人实验中，Masked IRL在数据使用效率、泛化能力和对模糊语言的鲁棒性方面均优于先前的方法，提升幅度可达15%。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在学习奖励函数时，由于数据有限而导致的过拟合和泛化能力不足的问题。现有方法未能有效利用语言指令来消除模糊性，导致模型专注于无关状态细节。

**核心思路**：Masked IRL通过结合示范和语言指令的互补信息，推断出状态相关性掩码，从而增强模型对无关状态的鲁棒性。该方法利用大语言模型的推理能力来澄清模糊指令，确保模型关注重要的状态信息。

**技术框架**：Masked IRL的整体架构包括两个主要模块：示范数据处理模块和语言指令解析模块。前者用于提取示范中的行为信息，后者则通过大语言模型解析指令并推断相关性掩码。

**关键创新**：本研究的主要创新在于将大语言模型与逆强化学习相结合，充分利用语言指令的潜力来消除奖励函数的模糊性。这一方法与传统的语言条件化奖励学习方法有本质区别，后者通常仅将语言作为简单的条件信号。

**关键设计**：在模型设计中，采用了特定的损失函数来优化状态相关性掩码的推断，同时在网络结构上结合了深度学习技术，以提高模型的学习效率和泛化能力。

## 📊 实验亮点

实验结果显示，Masked IRL在模拟和真实机器人任务中，相较于传统的语言条件化逆强化学习方法，性能提升可达15%。此外，该方法在数据使用效率上表现出色，使用的数据量减少至4.7倍，展现了更高的样本效率和对模糊语言的鲁棒性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在人机交互、服务机器人和自主系统等领域。通过提高机器人对用户偏好的理解能力，Masked IRL能够使机器人更好地适应复杂的任务环境，提升用户体验。未来，该方法也可能推动智能机器人在动态和不确定环境中的应用。

## 📄 摘要（原文）

> Robots can adapt to user preferences by learning reward functions from demonstrations, but with limited data, reward models often overfit to spurious correlations and fail to generalize. This happens because demonstrations show robots how to do a task but not what matters for that task, causing the model to focus on irrelevant state details. Natural language can more directly specify what the robot should focus on, and, in principle, disambiguate between many reward functions consistent with the demonstrations. However, existing language-conditioned reward learning methods typically treat instructions as simple conditioning signals, without fully exploiting their potential to resolve ambiguity. Moreover, real instructions are often ambiguous themselves, so naive conditioning is unreliable. Our key insight is that these two input types carry complementary information: demonstrations show how to act, while language specifies what is important. We propose Masked Inverse Reinforcement Learning (Masked IRL), a framework that uses large language models (LLMs) to combine the strengths of both input types. Masked IRL infers state-relevance masks from language instructions and enforces invariance to irrelevant state components. When instructions are ambiguous, it uses LLM reasoning to clarify them in the context of the demonstrations. In simulation and on a real robot, Masked IRL outperforms prior language-conditioned IRL methods by up to 15% while using up to 4.7 times less data, demonstrating improved sample-efficiency, generalization, and robustness to ambiguous language. Project page: https://MIT-CLEAR-Lab.github.io/Masked-IRL and Code: https://github.com/MIT-CLEAR-Lab/Masked-IRL

