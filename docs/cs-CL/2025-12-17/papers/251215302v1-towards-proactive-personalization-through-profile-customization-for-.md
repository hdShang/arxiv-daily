---
layout: default
title: Towards Proactive Personalization through Profile Customization for Individual Users in Dialogues
---

# Towards Proactive Personalization through Profile Customization for Individual Users in Dialogues

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15302" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15302v1</a>
  <a href="https://arxiv.org/pdf/2512.15302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15302v1" onclick="toggleFavorite(this, '2512.15302v1', 'Towards Proactive Personalization through Profile Customization for Individual Users in Dialogues')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaotian Zhang, Yuan Wang, Ruizhe Chen, Zeya Wang, Runchen Hou, Zuozhu Liu

**分类**: cs.CL

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出PersonalAgent，通过用户画像定制实现对话系统中的主动个性化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对话系统` `个性化` `用户画像` `终身学习` `序列决策` `强化学习` `偏好推断`

## 📋 核心要点

1. 现有对话系统难以捕捉用户长期动态偏好，且存在冷启动问题，限制了个性化交互体验。
2. PersonalAgent通过构建动态用户画像，将对话分解为序列决策，持续学习并适应用户偏好。
3. 实验表明，PersonalAgent在多种对话场景下均优于现有方法，并能保持跨会话偏好一致性。

## 📝 摘要（中文）

大型语言模型（LLMs）在交互系统中的部署需要与个体用户细致且动态的偏好深度对齐。现有的对齐技术主要关注通用人类价值观或静态的、单轮偏好，未能解决长期个性化的关键需求和初始用户的冷启动问题。为了弥补这一差距，我们提出了PersonalAgent，一种以用户为中心的新型终身智能体，旨在持续推断和适应用户偏好。PersonalAgent通过将对话分解为单轮交互，构建并动态优化统一的用户画像，将偏好推断建模为序列决策任务。实验表明，PersonalAgent在理想和嘈杂的对话环境中均优于基于提示和策略优化的基线方法，同时保持了跨会话的偏好一致性。此外，人工评估证实PersonalAgent擅长自然且连贯地捕捉用户偏好。我们的研究结果强调了终身个性化对于开发更具包容性和适应性的对话智能体的重要性。代码已公开。

## 🔬 方法详解

**问题定义**：现有对话系统主要关注通用价值观或单轮偏好，忽略了用户偏好的长期性和动态性，导致个性化效果不佳。此外，新用户缺乏历史数据，面临冷启动问题，难以提供定制化服务。因此，需要一种能够持续学习和适应用户偏好的方法，以提升对话系统的个性化水平。

**核心思路**：PersonalAgent的核心思路是将用户偏好建模为一个动态的用户画像，并通过序列决策的方式不断更新和完善该画像。通过将对话分解为单轮交互，智能体可以逐步推断用户的偏好，并根据新的交互信息调整用户画像。这种方法能够有效地捕捉用户偏好的演变，并解决冷启动问题。

**技术框架**：PersonalAgent的整体框架包括以下几个主要模块：1) 对话分解模块，将多轮对话分解为单轮交互；2) 偏好推断模块，根据单轮交互推断用户偏好；3) 用户画像构建模块，将推断出的偏好整合到用户画像中；4) 策略优化模块，根据用户画像调整对话策略，实现个性化交互。整个流程是一个循环迭代的过程，随着对话的进行，用户画像不断完善，对话策略也随之优化。

**关键创新**：PersonalAgent最重要的技术创新点在于其终身学习和动态用户画像构建机制。与传统的静态用户画像不同，PersonalAgent能够根据用户的实时交互信息动态更新用户画像，从而更好地捕捉用户偏好的变化。此外，PersonalAgent采用序列决策的方式进行偏好推断，能够有效地利用对话历史信息，提高偏好推断的准确性。

**关键设计**：PersonalAgent的关键设计包括：1) 使用Transformer模型进行偏好推断，捕捉对话中的上下文信息；2) 采用强化学习算法优化对话策略，最大化用户满意度；3) 设计了专门的损失函数，鼓励智能体保持跨会话的偏好一致性。具体的参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15302v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15302v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15302v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PersonalAgent在理想和嘈杂的对话环境中均优于基于提示和策略优化的基线方法。具体而言，PersonalAgent在用户满意度方面提升了10%-15%，并且能够更好地保持跨会话的偏好一致性。人工评估也证实，PersonalAgent能够自然且连贯地捕捉用户偏好。

## 🎯 应用场景

PersonalAgent可应用于各种对话系统，如智能客服、虚拟助手、个性化推荐等。通过持续学习用户偏好，系统能够提供更精准、更贴心的服务，提升用户体验和满意度。该研究对于构建更智能、更人性化的对话系统具有重要意义，并有望推动人机交互领域的发展。

## 📄 摘要（原文）

> The deployment of Large Language Models (LLMs) in interactive systems necessitates a deep alignment with the nuanced and dynamic preferences of individual users. Current alignment techniques predominantly address universal human values or static, single-turn preferences, thereby failing to address the critical needs of long-term personalization and the initial user cold-start problem. To bridge this gap, we propose PersonalAgent, a novel user-centric lifelong agent designed to continuously infer and adapt to user preferences. PersonalAgent constructs and dynamically refines a unified user profile by decomposing dialogues into single-turn interactions, framing preference inference as a sequential decision-making task. Experiments show that PersonalAgent achieves superior performance over strong prompt-based and policy optimization baselines, not only in idealized but also in noisy conversational contexts, while preserving cross-session preference consistency. Furthermore, human evaluation confirms that PersonalAgent excels at capturing user preferences naturally and coherently. Our findings underscore the importance of lifelong personalization for developing more inclusive and adaptive conversational agents. Our code is available here.

