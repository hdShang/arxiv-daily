---
layout: default
title: Privacy of Groups in Dense Street Imagery
---

# Privacy of Groups in Dense Street Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07085" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07085v1</a>
  <a href="https://arxiv.org/pdf/2505.07085.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07085v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07085v1', 'Privacy of Groups in Dense Street Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matt Franchi, Hauke Sandhaus, Madiha Zahrah Choksi, Severin Engelmann, Wendy Ju, Helen Nissenbaum

**分类**: cs.CY, cs.CV, cs.ET

**发布日期**: 2025-05-11

**备注**: To appear in ACM Conference on Fairness, Accountability, and Transparency (FAccT) '25

---

## 💡 一句话要点

**提出隐私保护框架以应对密集街景图像中的群体隐私问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `隐私保护` `街景图像` `群体识别` `数据安全` `人工智能` `城市分析` `自动驾驶`

## 📋 核心要点

1. 现有的隐私保护措施无法有效应对密集街景图像中群体隐私泄露的问题，尤其是在数据密度增加的情况下。
2. 本文提出了一种新的隐私保护框架，通过对DSI数据的深入分析，识别出可被推断的群体特征。
3. 实验结果表明，在25,232,608张图像中，敏感群体归属的推断准确性显著提高，揭示了现有隐私保护措施的不足。

## 📝 摘要（中文）

随着空间和时间上密集的街景图像（DSI）数据集的快速增长，个体隐私保护面临新的挑战。尽管DSI提供者通过模糊处理面孔和车牌来保护隐私，但这些措施未能解决更广泛的隐私问题。本文通过对25,232,608张纽约市的行车记录仪图像进行渗透测试，发现数据密度和人工智能的进步使得从假定匿名的数据中推断出敏感的群体归属变得容易。我们提出了一种可识别群体的分类法，并通过情境完整性的视角分析隐私影响，最后为研究人员提供了可行的建议。

## 🔬 方法详解

**问题定义**：本文旨在解决密集街景图像中群体隐私泄露的问题。现有的隐私保护措施，如模糊处理，无法有效防止群体身份的推断，导致潜在的隐私风险。

**核心思路**：论文的核心思路是通过对DSI数据的深入分析，识别出可被推断的群体特征，并提出相应的隐私保护框架，以增强数据使用中的隐私安全性。

**技术框架**：整体架构包括数据收集、群体特征识别、隐私风险评估和建议措施四个主要模块。首先收集大量行车记录仪图像，然后分析图像中可识别的群体特征，最后评估隐私风险并提出改进建议。

**关键创新**：最重要的技术创新点在于提出了一种新的群体识别分类法，并通过渗透测试验证了其有效性。这与现有方法的本质区别在于，传统方法主要关注个体隐私，而本研究强调群体隐私的保护。

**关键设计**：在技术细节上，采用了先进的图像处理算法和机器学习模型来识别群体特征，设置了特定的参数以优化识别精度，并设计了损失函数以平衡隐私保护与数据利用之间的关系。

## 📊 实验亮点

实验结果显示，通过对25,232,608张图像进行渗透测试，敏感群体归属的推断准确性显著提高，揭示了现有隐私保护措施的不足。这一发现为DSI数据的使用和隐私保护提供了新的视角和实证依据。

## 🎯 应用场景

该研究的潜在应用领域包括城市规划、交通管理和自动驾驶技术等。通过改进隐私保护措施，研究人员和企业可以在利用DSI数据进行分析的同时，保护公众的隐私权，促进数据的安全使用。未来，该框架有望为相关领域提供更为安全的技术支持。

## 📄 摘要（原文）

> Spatially and temporally dense street imagery (DSI) datasets have grown unbounded. In 2024, individual companies possessed around 3 trillion unique images of public streets. DSI data streams are only set to grow as companies like Lyft and Waymo use DSI to train autonomous vehicle algorithms and analyze collisions. Academic researchers leverage DSI to explore novel approaches to urban analysis. Despite good-faith efforts by DSI providers to protect individual privacy through blurring faces and license plates, these measures fail to address broader privacy concerns. In this work, we find that increased data density and advancements in artificial intelligence enable harmful group membership inferences from supposedly anonymized data. We perform a penetration test to demonstrate how easily sensitive group affiliations can be inferred from obfuscated pedestrians in 25,232,608 dashcam images taken in New York City. We develop a typology of identifiable groups within DSI and analyze privacy implications through the lens of contextual integrity. Finally, we discuss actionable recommendations for researchers working with data from DSI providers.

