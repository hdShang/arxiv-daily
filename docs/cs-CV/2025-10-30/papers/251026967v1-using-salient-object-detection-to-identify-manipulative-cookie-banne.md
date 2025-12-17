---
layout: default
title: Using Salient Object Detection to Identify Manipulative Cookie Banners that Circumvent GDPR
---

# Using Salient Object Detection to Identify Manipulative Cookie Banners that Circumvent GDPR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26967" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26967v1</a>
  <a href="https://arxiv.org/pdf/2510.26967.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26967v1" onclick="toggleFavorite(this, '2510.26967v1', 'Using Salient Object Detection to Identify Manipulative Cookie Banners that Circumvent GDPR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Riley Grossman, Michael Smith, Cristian Borcea, Yi Chen

**分类**: cs.CY, cs.AI, cs.CV, cs.HC

**发布日期**: 2025-10-30

**备注**: Accepted to International AAAI Conference on Web and Social Media 2026 (ICWSM'26)

---

## 💡 一句话要点

**利用显著性目标检测识别规避GDPR的操纵性Cookie横幅**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `Cookie横幅` `GDPR` `审美操纵` `显著性目标检测` `隐私监管`

## 📋 核心要点

1. 现有研究对Cookie横幅的审美操纵现象的检测不够全面，缺乏客观的量化方法，难以准确评估其普遍程度。
2. 该论文利用显著性目标检测模型，客观地衡量Cookie横幅中各个元素的显著程度，从而更准确地识别审美操纵。
3. 实验结果表明，审美操纵现象比以往报告的更为普遍，且欧盟网站更倾向于使用审美操纵来应对隐私监管。

## 📝 摘要（中文）

本文旨在研究符合通用数据保护条例（GDPR）的Cookie横幅中，审美操纵（一种将用户注意力吸引到允许个人数据共享的按钮的设计策略）的出现频率。同时，评估这些横幅在多大程度上符合GDPR以及国家数据保护机构关于横幅设计的建议。研究人员访问了2579个网站，识别了所使用的Cookie横幅类型。虽然45%的相关网站具有完全合规的横幅，但38%的合规横幅存在审美操纵。与以往的审美操纵研究不同，本文使用计算机视觉模型进行显著性目标检测，以衡量每个横幅元素的显著性（即吸引注意力的程度）。这使得研究人员能够发现新的审美操纵类型（例如，按钮放置），并得出结论：审美操纵比之前报告的更为常见（38% vs 27%）。为了研究用户和/或网站位置对Cookie横幅设计的影响，研究人员纳入了欧盟（EU）内（隐私监管执行更为严格）和欧盟外的网站，分别从欧盟和美国（US）的IP地址访问网站。研究发现，13.9%的欧盟网站在用户来自美国时会更改其横幅设计，并且欧盟网站使用审美操纵的可能性比非欧盟网站高约48.3%，突显了它们对隐私监管的创新应对。

## 🔬 方法详解

**问题定义**：该论文旨在解决如何更准确、更客观地识别网站上违反GDPR规定的操纵性Cookie横幅的问题。现有方法主要依赖人工分析，主观性强，难以发现新的操纵类型，并且无法量化操纵程度。因此，需要一种自动化的、客观的方法来评估Cookie横幅的设计是否具有操纵性。

**核心思路**：该论文的核心思路是利用计算机视觉中的显著性目标检测技术，将Cookie横幅视为图像，通过分析图像中各个元素的显著程度来判断是否存在审美操纵。显著性高的元素更容易吸引用户的注意力，如果允许数据共享的按钮的显著性明显高于其他元素，则可以认为该横幅具有操纵性。

**技术框架**：该研究的整体流程包括以下几个步骤：1) 收集大量网站的Cookie横幅数据；2) 使用显著性目标检测模型计算每个横幅元素的显著性得分；3) 分析显著性得分，识别审美操纵类型；4) 比较欧盟和非欧盟网站的Cookie横幅设计，分析用户和网站位置对横幅设计的影响。

**关键创新**：该论文的关键创新在于将显著性目标检测技术应用于Cookie横幅的分析，从而实现对审美操纵的客观量化。与以往研究相比，该方法能够发现新的审美操纵类型，并更准确地评估其普遍程度。此外，该研究还分析了用户和网站位置对Cookie横幅设计的影响，揭示了网站对隐私监管的应对策略。

**关键设计**：该研究使用了现有的显著性目标检测模型，具体模型的选择在论文中未明确说明（未知）。关键在于如何定义和量化审美操纵。研究人员可能定义了一系列指标，例如允许数据共享的按钮的显著性得分与其他按钮的显著性得分之比，或者允许数据共享的按钮的显著性得分与整个横幅的平均显著性得分之比。具体的阈值设置可能需要根据实验结果进行调整。

## 📊 实验亮点

该研究发现，38%的符合GDPR的Cookie横幅存在审美操纵，这一比例高于以往研究报告的27%。此外，研究还发现，欧盟网站使用审美操纵的可能性比非欧盟网站高约48.3%，表明欧盟网站更倾向于通过设计手段来影响用户选择。13.9%的欧盟网站在用户来自美国时会更改其横幅设计，暗示了网站根据用户地理位置调整隐私策略的行为。

## 🎯 应用场景

该研究成果可应用于隐私监管机构对网站Cookie横幅合规性的自动审查，帮助识别和打击违反GDPR规定的操纵性设计。同时，可以为网站设计者提供指导，设计出更透明、更符合用户意愿的Cookie横幅，提升用户体验和数据隐私保护水平。未来，该方法可以扩展到其他类型的用户界面分析，例如广告设计、软件界面等。

## 📄 摘要（原文）

> The main goal of this paper is to study how often cookie banners that comply with the General Data Protection Regulation (GDPR) contain aesthetic manipulation, a design tactic to draw users' attention to the button that permits personal data sharing. As a byproduct of this goal, we also evaluate how frequently the banners comply with GDPR and the recommendations of national data protection authorities regarding banner designs. We visited 2,579 websites and identified the type of cookie banner implemented. Although 45% of the relevant websites have fully compliant banners, we found aesthetic manipulation on 38% of the compliant banners. Unlike prior studies of aesthetic manipulation, we use a computer vision model for salient object detection to measure how salient (i.e., attention-drawing) each banner element is. This enables the discovery of new types of aesthetic manipulation (e.g., button placement), and leads us to conclude that aesthetic manipulation is more common than previously reported (38% vs 27% of banners). To study the effects of user and/or website location on cookie banner design, we include websites within the European Union (EU), where privacy regulation enforcement is more stringent, and websites outside the EU. We visited websites from IP addresses in the EU and from IP addresses in the United States (US). We find that 13.9% of EU websites change their banner design when the user is from the US, and EU websites are roughly 48.3% more likely to use aesthetic manipulation than non-EU websites, highlighting their innovative responses to privacy regulation.

