---
layout: default
title: A Service Robot's Guide to Interacting with Busy Customers
---

# A Service Robot's Guide to Interacting with Busy Customers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17241" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17241v1</a>
  <a href="https://arxiv.org/pdf/2512.17241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17241v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17241v1', 'A Service Robot\'s Guide to Interacting with Busy Customers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Suraj Nukala, Meera Sushma, Leimin Tian, Akansel Cosgun, Dana Kulic

**分类**: cs.RO, cs.HC

**发布日期**: 2025-12-19

**备注**: Presented at ACRA 2025. 10 pages, 4 figures. Includes a user study (N=24) using the Temi robot evaluating speech, visual, and micromotion modalities

**期刊**: Proceedings of the 2025 Australasian Conference on Robotics and Automation (ACRA 2025)

---

## 💡 一句话要点

**研究服务机器人与忙碌顾客交互，优化沟通方式以提升用户体验**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `服务机器人` `人机交互` `多模态沟通` `注意力捕获` `意图传达`

## 📋 核心要点

1. 现有服务机器人与忙碌顾客交互时，沟通方式效率低下，难以有效吸引注意并清晰传达意图。
2. 研究对比语音、视觉和微动等多种模态，探索不同模态在注意力捕获和意图传达方面的作用。
3. 实验表明语音擅长吸引注意，视觉更利于意图表达，为服务机器人优化沟通策略提供指导。

## 📝 摘要（中文）

本研究探讨了服务机器人与忙碌顾客有效沟通的方式，着重考察了语音、视觉显示和微动姿势等常用沟通方式在模拟餐厅场景中的有效性。通过一项包含24名参与者的两部分用户研究，模拟Temi机器人的送货任务，参与者进行打字游戏（MonkeyType）以模拟忙碌状态。第一部分评估了非语言声音提示与基线条件在单杯递送任务中的注意力捕获效果。第二部分评估了语音、视觉显示、微动姿势及其多模态组合在双杯递送任务中传达特定意图（正确选择杯子）的有效性。结果表明，语音在捕获注意力方面非常有效，但在清晰传达意图方面效果较差。参与者认为视觉显示是传达意图最有效的模式，其次是语音，微动姿势排名最低。这些发现为优化服务机器人的沟通策略提供了见解，突出了注意力捕获和意图沟通在动态服务环境中提升用户体验的不同作用。

## 🔬 方法详解

**问题定义**：论文旨在解决服务机器人在与忙碌的顾客交互时，如何有效地吸引顾客的注意力并清晰地传达其意图的问题。现有方法通常采用单一的沟通方式，例如仅使用语音或视觉提示，但这些方法可能无法充分考虑到顾客的忙碌状态，导致沟通效率低下，用户体验不佳。因此，需要研究更有效的多模态沟通策略，以适应动态的服务环境。

**核心思路**：论文的核心思路是对比不同沟通模态（语音、视觉显示、微动姿势）在注意力捕获和意图传达方面的效果，并探索多模态组合的潜力。通过模拟真实的餐厅场景，让参与者在忙碌状态下与服务机器人交互，评估不同模态对用户体验的影响。这种方法能够更准确地反映实际应用中的情况，为优化服务机器人的沟通策略提供依据。

**技术框架**：研究采用两部分的用户研究。第一部分比较非语言声音提示与基线条件，评估注意力捕获效果。第二部分评估语音、视觉显示、微动姿势及其多模态组合在传达特定意图方面的有效性。研究使用Temi机器人模拟送货任务，参与者通过打字游戏模拟忙碌状态。通过问卷调查和行为数据分析，评估不同模态的有效性。

**关键创新**：论文的关键创新在于系统地比较了不同沟通模态在服务机器人与忙碌顾客交互中的作用，并区分了注意力捕获和意图传达这两个不同的沟通目标。现有研究通常只关注单一模态或笼统的沟通效果，而忽略了不同模态在不同沟通目标上的差异。

**关键设计**：研究的关键设计包括：1) 使用MonkeyType打字游戏模拟顾客的忙碌状态，更贴近实际场景；2) 采用Temi机器人作为实验平台，模拟真实的送货任务；3) 通过问卷调查和行为数据（如杯子选择的准确率）综合评估不同模态的有效性；4) 细致地分析了不同模态在注意力捕获和意图传达方面的差异。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17241v1/hero.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17241v1/right_vis.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17241v1/micromotions.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，语音在捕获注意力方面效果显著，但视觉显示在传达意图方面更胜一筹。参与者普遍认为视觉显示是传达意图最有效的模态，其次是语音，而微动姿势的效果相对较差。这些发现为服务机器人设计更有效的沟通策略提供了重要依据，例如在需要快速吸引注意时使用语音提示，而在需要清晰传达信息时则优先考虑视觉显示。

## 🎯 应用场景

该研究成果可应用于餐厅、酒店、医院等多种服务场景，提升服务机器人的交互效率和用户满意度。通过优化沟通策略，服务机器人能够更好地适应动态环境，减少对顾客的干扰，提高服务质量。未来，该研究可扩展到其他类型的服务机器人和更复杂的交互场景，例如导览机器人、陪伴机器人等。

## 📄 摘要（原文）

> The growing use of service robots in hospitality highlights the need to understand how to effectively communicate with pre-occupied customers. This study investigates the efficacy of commonly used communication modalities by service robots, namely, acoustic/speech, visual display, and micromotion gestures in capturing attention and communicating intention with a user in a simulated restaurant scenario. We conducted a two-part user study (N=24) using a Temi robot to simulate delivery tasks, with participants engaged in a typing game (MonkeyType) to emulate a state of busyness. The participants' engagement in the typing game is measured by words per minute (WPM) and typing accuracy. In Part 1, we compared non-verbal acoustic cue versus baseline conditions to assess attention capture during a single-cup delivery task. In Part 2, we evaluated the effectiveness of speech, visual display, micromotion and their multimodal combination in conveying specific intentions (correct cup selection) during a two-cup delivery task. The results indicate that, while speech is highly effective in capturing attention, it is less successful in clearly communicating intention. Participants rated visual as the most effective modality for intention clarity, followed by speech, with micromotion being the lowest ranked.These findings provide insights into optimizing communication strategies for service robots, highlighting the distinct roles of attention capture and intention communication in enhancing user experience in dynamic hospitality settings.

