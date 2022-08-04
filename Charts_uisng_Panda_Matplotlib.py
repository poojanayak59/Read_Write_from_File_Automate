import matplotlib.pyplot as plt
import pandas


def charts_function():
    var = pandas.read_excel("inventory_after_exercise.xlsx")
    # x = list(var['Supplier'])
    # y = list(var['Inventory'])
    fig = plt.figure()
    plt.subplot(2, 2, 1)
    var.groupby('Supplier')['Product No'].count().plot(kind="pie", legend=False, title="Count(Products) per supplier")
    plt.subplot(2, 2, 2)
    var.groupby('Supplier')['Inventory'].max().plot(kind="barh", legend=True, title="Max(Inventories) per supplier")
    plt.subplot(2, 2, 3)
    var.groupby('Supplier')['Total_Price'].sum().plot(kind="area", legend=True, title="Sum(Total_Price) per supplier")
    plt.subplot(2, 2, 4)
    var.groupby('Product No')['Price'].min().plot(kind="line", legend=True, title="Min(Price) per Product")
    # plt.bar(x, y)
    # ln.Line2D(x, y)
    plt.suptitle('Different Type of Plots')
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.4, hspace=0.4, top=0.93, bottom=0.06, left=0.05, right=0.95)
    plt.grid(True)
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.savefig("c1_all_type_plots_panda_matplotlib.jpeg")
    mng.full_screen_toggle()
    mng.resize(*mng.window.maxsize())
    plt.show()


"""
plt.plot(x, z, color='red', marker='o')
plt.title('Inventory per Supplier', fontsize=14)
plt.xlabel('Supplier', fontsize=14)
plt.ylabel('Inventory', fontsize=14)

plt.show()
"""
