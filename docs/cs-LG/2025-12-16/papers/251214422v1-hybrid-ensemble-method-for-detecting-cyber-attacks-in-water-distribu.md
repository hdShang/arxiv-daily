---
layout: default
title: Hybrid Ensemble Method for Detecting Cyber-Attacks in Water Distribution Systems Using the BATADAL Dataset
---

# Hybrid Ensemble Method for Detecting Cyber-Attacks in Water Distribution Systems Using the BATADAL Dataset

**arXiv**: [2512.14422v1](https://arxiv.org/abs/2512.14422) | [PDF](https://arxiv.org/pdf/2512.14422.pdf)

**作者**: Waqas Ahmed

**分类**: cs.CR, cs.LG

**发布日期**: 2025-12-16

**备注**: 18 pages, & figures

---

## 💡 一句话要点

**提出混合集成学习方法以解决水分配系统中网络攻击检测的类别不平衡与时间依赖性问题**

**关键词**: `网络攻击检测` `混合集成学习` `水分配系统` `时间序列分析` `类别不平衡处理` `堆叠学习` `工业控制系统安全` `BATADAL数据集`

## 📋 核心要点

1. 核心问题：BATADAL数据集存在类别不平衡、多变量时间依赖性和隐蔽攻击等挑战，影响网络攻击检测的准确性。
2. 方法要点：提出混合集成学习框架，结合随机森林、极限梯度提升和长短期记忆网络，利用堆叠学习提升检测性能。
3. 实验或效果：混合堆叠集成在攻击检测上达到F1分数0.7205和AUC 0.9826，显著优于单一模型。

## 📝 摘要（中文）

随着数字连接性的扩展，管理关键基础设施（如水分配系统）的工业控制系统的网络安全变得越来越重要。BATADAL基准数据是测试入侵检测技术的良好来源，但它提出了几个重要问题，如类别数量不平衡、多变量时间依赖性和隐蔽攻击。我们考虑一种混合集成学习模型，通过利用机器学习和深度学习模型的互补能力，增强水分配系统中网络攻击的检测能力。对三种基础学习器（随机森林、极限梯度提升和长短期记忆网络）进行了严格比较，并使用了七种集成类型，包括简单平均和基于逻辑回归元学习器的堆叠学习。随机森林分析确定了转化为时间和统计特征的重要预测因子，并使用合成少数类过采样技术（SMOTE）来克服类别不平衡问题。分析表明，单一长短期记忆网络模型性能较差（F1 = 0.000，AUC = 0.4460），但基于树的模型，尤其是极限梯度提升，表现良好（F1 = 0.7470，AUC = 0.9684）。随机森林、极限梯度提升和长短期记忆网络的混合堆叠集成得分最高，攻击类别的F1分数为0.7205，AUC为0.9826，表明模型精度和泛化能力之间的异构堆叠是有效的。所提出的框架为时间依赖的工业系统中的网络攻击检测建立了一个稳健且可扩展的解决方案，集成了时间学习和集成多样性，以支持关键基础设施的安全运行。

## 🔬 方法详解

论文提出一个混合集成学习框架，用于水分配系统中的网络攻击检测。整体框架包括三个基础学习器：随机森林（RF）、极限梯度提升（XGBoost）和长短期记忆网络（LSTM），通过简单平均和堆叠学习（使用逻辑回归作为元学习器）进行集成。关键技术创新点在于结合了基于树的机器学习模型（RF和XGBoost）与深度学习模型（LSTM），以利用它们在处理静态特征和时间序列数据上的互补优势。与现有方法的主要区别在于，该方法通过异构堆叠集成，有效整合了不同模型的精度和泛化能力，同时使用SMOTE处理类别不平衡问题，并基于随机森林分析提取时间和统计特征，增强了模型对多变量时间依赖性和隐蔽攻击的检测能力。

## 📊 实验亮点

最重要的实验结果是混合堆叠集成（RF、XGBoost和LSTM）在攻击检测上表现最佳，F1分数为0.7205，AUC高达0.9826，显著优于单一模型（如LSTM的F1为0.000）。这表明异构集成能有效提升检测性能，解决了类别不平衡和时间依赖性问题。

## 🎯 应用场景

该研究主要应用于工业控制系统的网络安全领域，特别是水分配系统等关键基础设施的网络攻击检测。实际价值在于提供了一种稳健且可扩展的解决方案，能够集成时间学习和模型多样性，支持关键基础设施的安全运行，并可能扩展到其他时间依赖的工业系统，如电力或交通控制系统。

## 📄 摘要（原文）

> The cybersecurity of Industrial Control Systems that manage critical infrastructure such as Water Distribution Systems has become increasingly important as digital connectivity expands. BATADAL benchmark data is a good source of testing intrusion detection techniques, but it presents several important problems, such as imbalance in the number of classes, multivariate time dependence, and stealthy attacks. We consider a hybrid ensemble learning model that will enhance the detection ability of cyber-attacks in WDS by using the complementary capabilities of machine learning and deep learning models. Three base learners, namely, Random Forest , eXtreme Gradient Boosting , and Long Short-Term Memory network, have been strictly compared and seven ensemble types using simple averaged and stacked learning with a logistic regression meta-learner. Random Forest analysis identified top predictors turned into temporal and statistical features, and Synthetic Minority Oversampling Technique (SMOTE) was used to overcome the class imbalance issue. The analyics indicates that the single Long Short-Term Memory network model is of poor performance (F1 = 0.000, AUC = 0.4460), but tree-based models, especially eXtreme Gradient Boosting, perform well (F1 = 0.7470, AUC=0.9684). The hybrid stacked ensemble of Random Forest , eXtreme Gradient Boosting , and Long Short-Term Memory network scored the highest, with the attack class of 0.7205 with an F1-score and a AUC of 0.9826 indicating that the heterogeneous stacking between model precision and generalization can work. The proposed framework establishes a robust and scalable solution for cyber-attack detection in time-dependent industrial systems, integrating temporal learning and ensemble diversity to support the secure operation of critical infrastructure.

