---
layout: default
title: Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization
---

# Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14263" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14263</a>
  <a href="https://arxiv.org/pdf/2512.14263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14263" onclick="toggleFavorite(this, '2512.14263', 'Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nick Leenders, Thomas Quadt, Boris Cule, Roy Lindelauf, Herman Monsuur, Joost van Oijen, Mark Voskuijl

**分类**: cs.LG, cs.AI, math.OC

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于决策树的可解释偏好学习模型，提升偏好贝叶斯优化在复杂场景下的性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `偏好学习` `贝叶斯优化` `决策树` `可解释性` `代理模型`

## 📋 核心要点

1. 现有偏好贝叶斯优化方法依赖高斯过程，存在可解释性差、难以处理分类数据和计算复杂度高等问题。
2. 论文提出一种基于决策树的代理模型，该模型具有可解释性，能够处理混合数据类型，并可扩展到大型数据集。
3. 实验表明，该模型在尖锐优化函数上优于高斯过程，并在真实寿司数据集上成功学习了个人偏好。

## 📝 摘要（中文）

现有的偏好贝叶斯优化方法依赖于高斯过程（GP）作为代理模型。这些模型难以解释，难以处理分类数据，并且计算复杂度高，限制了其在现实世界中的可用性。本文介绍了一种本质上可解释的、基于决策树的代理模型，该模型能够处理分类和连续数据，并且可以扩展到大型数据集。在八个日益尖锐的优化函数上进行的大量数值实验表明，我们的模型在尖锐函数上优于基于GP的替代方案，并且对于非尖锐函数，性能仅略有降低。此外，我们将我们的模型应用于真实的寿司数据集，并展示了其学习个人寿司偏好的能力。最后，我们展示了一些关于使用历史偏好数据来加速新用户的优化过程的初步工作。

## 🔬 方法详解

**问题定义**：现有的偏好贝叶斯优化方法主要依赖于高斯过程（GP）作为代理模型来建模用户的偏好。然而，GP模型存在一些固有的局限性，例如可解释性差，难以直接理解模型是如何做出决策的；难以有效处理包含分类变量的数据集；以及计算复杂度较高，难以扩展到大规模数据集。这些局限性限制了偏好贝叶斯优化在实际应用中的广泛使用。

**核心思路**：本文的核心思路是使用决策树作为偏好贝叶斯优化的代理模型，替代传统的高斯过程。决策树具有天然的可解释性，易于理解其决策过程。此外，决策树可以同时处理连续型和离散型数据，无需进行复杂的预处理。通过构建合适的决策树模型，可以有效地学习用户的偏好，并用于指导优化过程。

**技术框架**：该方法主要包含以下几个阶段：1) 收集用户的偏好数据，例如通过成对比较或排序等方式获取用户对不同选项的偏好关系。2) 使用收集到的偏好数据训练决策树模型，该模型的目标是预测用户对不同选项的偏好程度。3) 使用训练好的决策树模型作为代理模型，指导贝叶斯优化过程。在每次迭代中，根据决策树模型的预测结果选择下一个要评估的选项，并更新模型。4) 重复步骤3，直到达到预定的优化目标或迭代次数。

**关键创新**：该论文最重要的技术创新点在于将决策树引入到偏好贝叶斯优化中，替代了传统的高斯过程。这种方法不仅提高了模型的可解释性，使其更容易被用户理解和信任，而且能够有效地处理包含分类变量的数据集，并具有良好的可扩展性。此外，论文还探索了利用历史偏好数据加速新用户偏好学习的方法。

**关键设计**：论文中使用的决策树模型可以采用不同的算法进行构建，例如CART、ID3或C4.5等。关键的设计包括如何选择合适的决策树算法，如何设置决策树的深度和叶子节点数量等参数，以及如何处理偏好数据中的噪声和不一致性。此外，论文还可能涉及到如何设计合适的采集函数（Acquisition Function），用于在贝叶斯优化过程中选择下一个要评估的选项。具体的损失函数和网络结构取决于所选择的决策树算法和采集函数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14263/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14263/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14263/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该模型在尖锐优化函数上优于基于高斯过程的替代方案，表明其在复杂优化问题上的优势。在真实的寿司数据集上，该模型成功学习了个人的寿司偏好，验证了其在实际应用中的有效性。此外，初步实验表明，利用历史偏好数据可以加速新用户的偏好学习过程，为进一步提升优化效率提供了可能。

## 🎯 应用场景

该研究成果可应用于个性化推荐系统、产品设计、用户界面优化等领域。例如，可以利用该模型学习用户的口味偏好，从而推荐更符合用户口味的菜品或商品。在产品设计中，可以根据用户对不同设计方案的偏好，优化产品的功能和外观。此外，该方法还可以用于优化用户界面，提高用户体验。未来，该方法有望在更多需要理解和建模用户偏好的场景中得到应用。

## 📄 摘要（原文）

> Current Preferential Bayesian Optimization methods rely on Gaussian Processes (GPs) as surrogate models. These models are hard to interpret, struggle with handling categorical data, and are computationally complex, limiting their real-world usability. In this paper, we introduce an inherently interpretable decision tree-based surrogate model capable of handling both categorical and continuous data, and scalable to large datasets. Extensive numerical experiments on eight increasingly spiky optimization functions show that our model outperforms GP-based alternatives on spiky functions and has only marginally lower performance for non-spiky functions. Moreover, we apply our model to the real-world Sushi dataset and show its ability to learn an individual's sushi preferences. Finally, we show some initial work on using historical preference data to speed up the optimization process for new unseen users.

